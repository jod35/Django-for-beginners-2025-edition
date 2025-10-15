from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from products.forms import ProductCreateForm
from .data import products
from .models import Product
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse
# Create your views here.


class HomepageView(ListView):
    page_title = "Product List"
    template_name = "index.html"
    model = Product
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.page_title
        return context


class AboutPage(TemplateView):
    page_title = "About Page"
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context


class ContactPage(TemplateView):
    page_title = "Contact Page"
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

class ProductCreateView(TemplateView):
    template_name = 'products/product_creation_form.html'
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request:HttpRequest):

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('homepage'))
        return redirect(reverse('product_create'))