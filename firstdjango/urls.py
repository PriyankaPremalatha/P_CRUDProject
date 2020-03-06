"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('home/', views.home),

    

    path('crud/', views.CrudView.as_view(),name='crud'),

    path('ajax/crud/create/', views.CreateCrudUser.as_view(),name='crudcreate'),

    path('ajax/crud/update/', views.UpdateCrudUser.as_view(),name='crudupdate'),

    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(),name='cruddelete'),

    path('crudregister/', views.Crudregister.as_view(),name='crudregister'),

    path('registration/', views.CreateRegisterUser.as_view(),name='registrationuser'),

    path('user_login/',views.user_login,name='user_login')    

    
]
