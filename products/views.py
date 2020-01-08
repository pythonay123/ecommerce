from django.shortcuts import render
from django.urls import reverse
from .models import Product


# Create your views here.
def home(request):
    all_products = Product.objects.all()
    template = 'products/home.html'
    context = {'products': all_products}
    return render(request, template, context)


def all(request):
    all_products = Product.objects.all()
    context = {'products': all_products}
    template = 'products/all.html'
    return render(request, template, context)
