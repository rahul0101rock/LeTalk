

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
def index(request):
    template = loader.get_template('chat/index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('chat/login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('chat/register.html')
    return HttpResponse(template.render())