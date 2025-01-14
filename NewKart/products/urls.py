from django.urls import path
from . views import IndexView,ProductList,About,ProductsDetails


urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('products/',ProductList,name='products'),
    path('about/',About.as_view(),name='about'),
    path('products_details/<int:pk>/', ProductsDetails.as_view(), name='products_details')
]