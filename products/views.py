from django.shortcuts import render
from django.urls import reverse


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
