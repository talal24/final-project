from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'base/', views.home, name='base'),
    path(r'product/<int:id>/', views.product, name='product'),
    path(r'products/', views.products, name='products'),
    path(r'add-product/', views.add_product, name='add-product'),
    path(r'delete-product/', views.delete_product, name='delete-product')

]
