from django.shortcuts import render
from django.urls import reverse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


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


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        template = 'products/single.html'
        return render(request, template, context)
    except ObjectDoesNotExist:
        raise Http404
