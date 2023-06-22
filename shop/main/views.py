from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контактная информация'})


def payment(request):
    return render(request, 'main/payment.html', {'title': 'Доставка и оплата'})


def cart(request):
    return render(request, 'main/cart.html', {'title': 'Корзина'})
