from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# map url /products to the function index
def index(request):
    products = Product.objects.all()
    return render(request, 
                  'index.html', 
                  {'products':products})


def new_product(request):
    return HttpResponse("New product!")