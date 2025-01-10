from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from . models import Product

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'
    
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by = 12
    
class About(TemplateView):
    template_name = 'about.html'

class ProductsDetails(TemplateView):
    template_name = 'products_details.html'
    