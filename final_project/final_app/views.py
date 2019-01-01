from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.

def home(request):
    title = 'Home Page'
    context = {'title': title}
    return render(request, 'home.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product(request, id):
    product = Product.objects.filter(id=id)
    title = 'Home Page'
    context = {'title': title, 'product': product}
    return render(request, 'home.html', context)


def add_product(request):
    # product = Product.objects.get(id=5)
    form = ProductForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save(commit=False)

        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)


def delete_product(request, id):
    product = Product.objects.get(id=id)
    instance = product
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            instance.delete()
        print("this is post page")
    context = {'form': form}
    return render(request, 'delete_product.html', context)
