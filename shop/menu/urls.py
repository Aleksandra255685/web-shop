from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('<slug:slug>/', views.ProductView.as_view(), name='product_view'),
]
