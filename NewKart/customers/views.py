from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Customer

# Create your views here.

class LogIn(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    # redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('index')
    
    
# customers/views.py

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):  # Renamed from create_customer
    if created:
        Customer.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    if hasattr(instance, 'customer'):
        instance.customer.save()
        
def create_customer_view(request):
    if request.user.is_authenticated:
        Customer.objects.get_or_create(
            user=request.user,
            defaults={'name': request.user.username}
        )
        return redirect('cart')
    return redirect('login')