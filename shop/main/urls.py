from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('cart', views.cart, name='cart')
]
