from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("about/", views.AboutPage.as_view(), name="about_page"),
    path("contact/", views.ContactPage.as_view(), name="contact_page"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
]
