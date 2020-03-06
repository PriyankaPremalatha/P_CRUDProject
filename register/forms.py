from django import forms
from register.models import CrudUserRegister

class RegisterForm(forms.ModelForm):
	class Meta:
		model= CrudUserRegister
		fields= "__all__"

		