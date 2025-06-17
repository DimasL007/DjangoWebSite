from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services_view, name='services'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('products/', views.product_list_view, name='product_list'),

]
