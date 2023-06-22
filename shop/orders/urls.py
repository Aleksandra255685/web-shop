from django.urls import include, re_path
from . import views

app_name = 'orders'
urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]
