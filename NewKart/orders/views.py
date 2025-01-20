from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView
from . models import Order, OrderedItem
from products.models import Product
from django.http import JsonResponse
from customers.models import Customer
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def cart_view(request):
    user = request.user
    try:
        customer = user.customer
    except Customer.DoesNotExist:
        return redirect('create_customer')
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    total_price = sum(item.product.price * item.quantity for item in cart_obj.added_items.all())
     
    context = {'cart': cart_obj,
                'total_price': total_price
               }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        user=request.user
        customer = user.customer
        quantity=request.POST.get('quantity',1)
        product = Product.objects.get(pk=product_id)
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        OrderedItem.objects.create(
            product=product,
            owner=cart_obj,
            quantity=quantity
        )
    return redirect('cart') 


def update_cart_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity',1))
        
        item = get_object_or_404(OrderedItem, id=item_id)
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
            
        return JsonResponse({'success': True})
    
    return JsonResponse({'success':False}, status=400)

def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderedItem, id= item_id)
    item.delete()
    return redirect('cart')  
    
def checkout(request):
    if request.method == 'POST':
        # Collect checkout form data and save to session
        request.session['checkout_data'] = request.POST
        return HttpResponseRedirect('/payment/')
    return render(request, 'checkout.html')

def payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('paymentMethod')
        
        return render(request, 'payment.html')
    return render(request, 'payment.html')

def payment_success(request):
    return render(request, 'payment_success.html')
