from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def home_view(request):
    return render(request, 'home.html', {'title': 'Home'})

def about_view(request):
    return render(request, 'about.html', {'title': 'About'})

def contact_view(request):
    return render(request, 'contact.html', {'title': 'Contact'})

def services_view(request):
    return render(request, 'services.html', {'title': 'Services'})

def gallery_view(request):
    return render(request, 'gallery.html', {'title': 'Gallery'})
