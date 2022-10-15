from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs = {'class': 'form-control'}





	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control'}))