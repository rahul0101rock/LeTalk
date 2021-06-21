

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.files.storage import FileSystemStorage
from django.db import models
from .forms import SignUpForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import user_search,friends_list,request_list
f = FileSystemStorage(location='/media')
def index(request):
    context = {}
    if request.user.is_authenticated:
        users=User.objects.all()
        context["user_search"]=users
        user = request.user
        if request.method == 'POST':
                r_user= request.POST.get("r_user")
                if r_user:
                    rv = User.objects.get(username=r_user)
                    fr = request_list.objects.filter(sender=user, receiver=rv)
                    if len(fr)==0:
                        if len(friends_list.objects.filter(user=user))==0:flo = friends_list.objects.create(user=user)
                        else: flo = friends_list.objects.get(user=user)
                        flo.add_in_list(rv)
                        fr_rq = request_list(sender=user, receiver=rv)
                        fr_rq.save()
        u = User.objects.get(username=user)
        rq = request_list.objects.filter(receiver=u)
        fl=[]
        if len(friends_list.objects.filter(user=user))==0:flo = friends_list.objects.create(user=user)
        else: flo = friends_list.objects.get(user=user)
        for fr in flo.friends.all():fl.append(fr)
        context["requests"]=rq
        context["friends"]=fl
    return render(request, 'chat/index.html',context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, 'Username or Password is Incorrect')
                return redirect('login')
        else:
            return render(request, 'chat/login.html', {})
def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
    	if request.method =='POST':
    		form = SignUpForm(request.POST)
    		if form.is_valid():
    			form.save()
    			username = form.cleaned_data['username']
    			password = form.cleaned_data['password1']
    			user = authenticate(username=username, password=password)
    			login(request,user)
    			return redirect('/')
    	else:
    		form = SignUpForm()
    	return render(request, 'chat/register.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
    	logout(request)
    	return redirect('/')
    else:
        return redirect('/login')

def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = EditProfileForm(request.POST, instance= request.user)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = EditProfileForm(instance= request.user)
        return render(request, 'chat/profile.html', {'form': form})
    else:
        return redirect('/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = PasswordChangeForm(data=request.POST, user= request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Changed Successfully.')
                return redirect('/change_password')
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request, 'chat/change_password.html', {'form': form})
    else:
        return redirect('/')




