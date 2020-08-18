from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import auth
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)


def productA(request, pk):
    prod = Product.objects.get(id=pk)

    context = {'prod': prod}

    return render(request, 'product-details.html', context)


def add_item(request):
    if request.method == 'POST':
        prodid = request.POST['prodid']
        qty = request.POST['qty']
        item = Product.objects.get(id=prodid)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderitem = OrderItem(product=item, order=order, value=qty)
        orderitem.save()
        return JsonResponse({'message': 'Success'})


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
        return render(request, 'account.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pas = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=pas)
        customer = Customer(user=user, name=name, email=email)
        customer.save()
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
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


def payment(request):
    return HttpResponse('<h1>Payment successfully complete!</h1>')
