from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    categoryId = request.GET.get('category')
    products = products.filter(sub_category=categoryId) if categoryId else products
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context)
