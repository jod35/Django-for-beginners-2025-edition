from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/',views.about_page ,name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
]