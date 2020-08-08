from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Pizza-Order Project/index.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pizza-Order Project/product.html', context)


def productA(request, pk):
    prod = Product.objects.get(id=pk)

    context = {'prod': prod, }

    return render(request, 'pizza-Order Project/product-details.html', context)


def account(request):
    if request.method == 'POST':
        name = request.POST['name']
        # Email = request.POST['email']
        pas = request.POST['password']

        user = auth.authenticate(username=name, password=pas)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'invalid info please make sure username & password')
            return redirect('/account')
    else:
        return render(request, 'Pizza-Order Project/account.html')
    # return render(request, 'Pizza-Order Project/account.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'Pizza-Order Project/register.html')

    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pas = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=pss)
        return redirect('Account')


def user_logout(request):
    logout(request)
    return redirect('/')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'Pizza-Order Project/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'Pizza-Order Project/checkout.html', context)


def payment(request):
    return HttpResponse('<h1>Payment successfully complete!</h1>')
