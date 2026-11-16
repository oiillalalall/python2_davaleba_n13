from django.shortcuts import render
from django_app.models import Book, Author


def home(request):
    return render(request, 'home.html')

def products(request):
    products = Book.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def product(request, id):
    product = Book.objects.filter(id=id).first()
    context = {'product': product}
    return render(request, 'product.html', context)
# Create your views here.
