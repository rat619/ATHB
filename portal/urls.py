from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about')
]
