from django.shortcuts import render
from .models import Cart


# Create your views here.
def view(request):
    cart = Cart.objects.all()[0]
    template = 'carts/view.html'
    context = {'cart': cart}
    return render(request, template, context)
