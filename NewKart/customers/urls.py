from django.urls import path
from . views import LogIn,RegisterView,logout_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',LogIn.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',logout_view,name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]