from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart_item/', views.update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('confirm-payment/',views.payment,name='payment'),
    path('payment_success/',views.payment_success,name='payment_success'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
