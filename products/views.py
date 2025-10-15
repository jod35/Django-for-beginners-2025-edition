from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .data import products
from .models import Product
from django.views.generic import ListView, TemplateView, DetailView

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