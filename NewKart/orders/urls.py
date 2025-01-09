from django.urls import path
from . views import CartList


urlpatterns = [
    path('cart/',CartList.as_view(),name='cart')
]