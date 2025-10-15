from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from products.forms import ProductCreateForm
from .data import products
from .models import Product
# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
    page_title = "Product List"
    product_list = Product.objects.all()
    return render(request,'index.html',
                  {'title': page_title, 'products': product_list})

def about_page(request: HttpRequest) -> HttpResponse:
    page_title = "About Page"
    return render(request,'about.html',{'title': page_title})

def contact_page(request: HttpRequest) -> HttpResponse:
    page_title = "Contact Page"
    return render(request,'contact.html',{'title': page_title})
