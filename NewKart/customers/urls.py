from django.urls import path
from . views import LogIn,Register


urlpatterns = [
    path('login/',LogIn.as_view(),name='login'),
    path('register/',Register.as_view(),name='register')
]