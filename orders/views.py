from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from django.urls import reverse
from .models import Order
import time


# Create your views here.
def checkout(request):
    try:
        id = request.session['cart_id']
        cart = Cart.objects.get(id=id)
    except (KeyError, Cart.DoesNotExist):
        id = None
        return HttpResponseRedirect(reverse('cart_view'))
    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        # Assign a user to the order
        new_order.order_id = str(time.time())
        new_order.save()

    # Run credit card
    # Assign address to the order
    if new_order.status == "completed":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart_view'))

    context = {}
    template = 'products/home.html'
    return render(request, template, context)
