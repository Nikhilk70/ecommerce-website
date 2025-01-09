from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LogIn(TemplateView):
    template_name = 'login.html'
    
class Register(TemplateView):
    template_name = 'register.html'