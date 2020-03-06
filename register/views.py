from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse
from .models import CrudUser,CrudUserRegister
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


def home(request):
	 return render(request,'home.html')


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud.html'
    context_object_name = 'users'


class CreateCrudUser(View):
	def get(self, request):
		name1=request.GET.get('name',None)
		address1=request.GET.get('address',None)
		age1=request.GET.get('age',None)


		obj=CrudUser.objects.create(

			name=name1,
			address=address1,
			age=age1,

			)
		user={'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

		data={ 'user':user}
		return JsonResponse(data)

class UpdateCrudUser(View):
	def get(self, request):

		id1=request.GET.get('id',None)
		name1=request.GET.get('name',None)
		address1=request.GET.get('address',None)
		age1=request.GET.get('age',None)

		obj=CrudUser.objects.get(id=id1)
		obj.name=name1
		obj.address=address1
		obj.age=age1
		obj.save()

		user={'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

		data={ 'user':user}
		
		return JsonResponse(data)



class DeleteCrudUser(View):
	def get(self,request):
		id1=request.GET.get('id',None)
		CrudUser.objects.get(id=id1).delete()
		data={ 'deleted':True}
		return JsonResponse(data)




# user registration
class Crudregister(ListView):
    model = CrudUserRegister
    template_name = 'registration.html'
    context_object_name = 'regusers'

class CreateRegisterUser(View):
 	def get(self, request):
 		fname1=request.GET.get('firstname',None)
 		lname1=request.GET.get('lastname',None)
 		email1=request.GET.get('email',None)
 		mobile1=request.GET.get('mobile',None)
 		password1=request.GET.get('password',None)
 		conpassword1=request.GET.get('conpassword',None)


 		
 		obj=CrudUserRegister.objects.create(

 			firstname=fname1,
 			lastname=lname1,
 			email=email1,
 			mobile=mobile1,
 			password=password1,

 		)
 		user={'id':obj.id,'firstname':obj.firstname,'lastname':obj.lastname,'email':obj.email,'mobile':obj.mobile,'password':obj.password}

 		data={ 'user':user}
 		return JsonResponse(data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST('email')
        password = request.POST('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'home.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'login.html')