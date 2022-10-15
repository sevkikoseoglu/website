from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import  render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def register_request(request):
	request_form = RegisterForm()
	if request.method == "POST":
		request_form = RegisterForm(request.POST)
		if request_form.is_valid():
			user = request_form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	return render (request=request, template_name="register.html", context={'form': request_form})

def login_request(request):
	login_form = LoginForm()
	if request.method == "POST":
		login_form = LoginForm(request, data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={'form': login_form})

def homepage(request):
	return render(request=request, template_name="homepage.html")

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))