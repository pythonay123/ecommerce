from django.shortcuts import render
from django.urls import reverse
from .models import Product


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        #     user_name = 'Justin is the current user'
        # else:
        #     user_name = 'Unknown'
        user_name = request.user
    else:
        user_name = request.user
    context = {'user_name': user_name}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    all_products = Product.objects.all()
    context = {'products': all_products}
    template = 'products/all.html'
    return render(request, template, context)
