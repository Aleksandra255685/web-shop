from django.shortcuts import render
from django.views import View

from .models import Product


class MenuView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'menu/menu.html', {'products_list': products})


class ProductView(View):
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        return render(request, 'menu/product.html', {'product': product})
