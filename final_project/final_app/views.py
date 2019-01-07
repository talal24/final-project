from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm


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
            form.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)


def delete_product(request, id):
    form = get_object_or_404(Product, id=id)
    # instance = product
    # form = ProductForm(instance=product)
    if request.method == 'POST':
        # form = form(request.POST)
        # if form.is_valid():
        #     print(form.errors)
        form.delete()
        print("this is post page")
    context = {'form': form}
    return render(request, 'delete_product.html', context)


def signup(request):
    form = SignUpForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'signup.html', context)
    else:
        return render(
            request,
            'signup.html', context)


def update_product(request, id):
    product = Product.objects.filter(id=id).first()
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            print(form.errors)
            instance.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'update_form.html', context)
