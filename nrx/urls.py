from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_list, name='product'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('main/', views.main, name='main'),
]