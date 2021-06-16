

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.files.storage import FileSystemStorage
from django.db import models
from .forms import SignUpForm
from django.contrib import messages
f = FileSystemStorage(location='/media')

def index(request):
    template = loader.get_template('chat/index.html')
    return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('/')
        else:return redirect('login')
    else:
        return render(request, 'chat/login.html', {})
def register(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'chat/register.html', {'form': form})

def profile(request):
    template = loader.get_template('chat/profile.html')
    return HttpResponse(template.render())