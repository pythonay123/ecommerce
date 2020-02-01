from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart
from products.models import Product


# Create your views here.
def view(request):
    cart = Cart.objects.all()[0]
    template = 'carts/view.html'
    context = {'cart': cart}
    return render(request, template, context)


def update_cart(request, product_slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist as err:
        print(err)
    except Exception:
        pass
    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart_view"))
