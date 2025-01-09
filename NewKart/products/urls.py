from django.urls import path
from . views import Index,ProductList,About,ProductsDetails


urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('products/',ProductList.as_view(),name='products'),
    path('about/',About.as_view(),name='about'),
    path('products_detials/',ProductsDetails.as_view(),name='products_detials')
]