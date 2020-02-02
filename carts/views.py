from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Product


# Create your views here.
def view(request):
    try:
        _id = request.session['cart_id']
    except:
        _id = None
    if _id:
        cart = Cart.objects.get(id=_id)
        context = {'cart': cart}
    else:
        empty_message = "Your cart is empty, please shop with us."
        context = {"empty": True, "empty_message": empty_message}

    template = 'carts/view.html'
    return render(request, template, context)


def update_cart(request, product_slug, qty):
    request.session.set_expiry(900)
    try:
        _id = request.session['cart_id']
    except Exception:
        new_chart = Cart()
        new_chart.save()
        request.session['cart_id'] = new_chart.id
        _id = new_chart.id
    cart = Cart.objects.get(id=_id)
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist as err:
        print(err)
    except Exception:
        pass
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        pass
    if qty == 0:
        cart_item.quantity = 0
        cart_item.delete()
    else:
        cart_item.quantity = qty
        cart_item.save()
    # if cart_item not in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    new_total = 0.00
    for item in cart.cartitem_set.all():
        brand_total = float(item.product.price) * item.quantity
        new_total += brand_total

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart_view"))
