from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'
    
class ProductList(TemplateView):
    template_name = 'product.html'
    
class About(TemplateView):
    template_name = 'about.html'

class ProductsDetails(TemplateView):
    template_name = 'products_details.html'
    