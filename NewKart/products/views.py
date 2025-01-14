from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'featured_products': Product.objects.order_by('priority')[:3]}
    
def ProductList(request):
    page_number = int(request.GET.get('page',1))
    products = Product.objects.order_by('priority')
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'product.html',{'page_obj': page_obj})
    
class About(TemplateView):
    template_name = 'about.html'

class ProductsDetails(DetailView):
    model = Product
    template_name = 'products_details.html'
    contet_object_name = 'product'
    
# def index(request):
#     featured_products = Product.objects.order_by('priority')[:4]
#     context = {'featured_products':featured_products}
#     return render(request,'index.html',context)