import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    if request.method == "GET":
        if request.GET.get("edit") is not None:
            return render(request, 'store/product/edit_product.html.jinja2', context)
        else:
            return render(request, 'store/product/detail.html.jinja2', context)

    elif request.method == "POST":
        keys = ('name', 'size', 'price', 'quantity')
        if all((key in request.POST for key in keys)):
            for key in keys:
                setattr(product, key, request.POST[key])
            try:
                product.save()
            except ValidationError as e:
                context["notifications"] = []
                #add validation
                # print(e)
                context["notifications"].append("Validation Error")
                return render(request, 'store/product/edit_product.html.jinja2',context)
            return render(request, 'store/product/detail.html.jinja2', context)

    elif request.method == "DELETE":
        if product is not None:
            product.delete()
        return redirect(index)


def add_product(request):
    if request.method == "GET":
        return render(request, 'store/product/add_product.html.jinja2')
    elif request.method == "POST":
        keys = ('name', 'size', 'price', 'quantity')
        if all((key in request.POST for key in keys)):
            product = Product.objects.create(**{key: request.POST[key] for key in keys})
            product.save()
            return redirect(product_view, pk=product.pk)


def view_user(request):
    if request.method == "GET":
        return render(request, 'customers/view_user.html.jinja2')
    elif request.method == "POST":
        keys = ('username', 'size', 'price', 'quantity')
        if all((key in request.POST for key in keys)):
            for key in keys:
                setattr(product, key, request.POST[key])
            try:
                product.save()
            except ValidationError as e:
                context["notifications"] = []
                #add validation
                # print(e)
                context["notifications"].append("Validation Error")
                return render(request, 'store/product/edit_product.html.jinja2',context)
            return render(request, 'store/product/detail.html.jinja2', context)


def index(request):
    return render(request, 'store/product/list.html.jinja2', {'products': Product.objects.all()})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')

    elif request.method == 'GET':
        return render(request, 'registration/login.html.jinja2')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # User.objects.create_user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('list')

        else:
            return redirect('login')

    elif request.method == 'GET':
        return render(request, 'registration/register.html.jinja2', {})


def logout(request, context=None):
    if request.method == 'POST':
        request.session.clear()
        return redirect('list')

    elif request.method == 'GET':
        return render(request, 'store/product/list.html.jinja2', {})


def cart(request):
    if request.method == 'POST':
        action = request.POST.get("action", None)
        if action == "add_to_cart" or action == "remove_from_cart":
            product_id = request.POST.get("product_id", None)
            if product_id is not None and product_id.isnumeric():
                product = Product.objects.get(pk=product_id)
                if product is not None:
                    cart = str(request.session.get("cart", "")).split(",")
                    if action == "add_to_cart":
                        cart.append(product_id)
                        product.quantity -= 1
                    else:
                        cart.remove(product_id)
                        product.quantity += 1
                    request.session["cart"] = ",".join([i for i in cart if i != ""])
                    return HttpResponse(status=200)
                else:
                    return HttpResponse(status=404)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(content="unknown action", status=400)
    elif request.method == 'GET':
        cart = request.session.get("cart")
        products = []
        if cart is not None:
            cart = list(filter(str.isnumeric, cart.split(",")))
            for product_id in cart:
                product = Product.objects.get(pk=product_id)
                if product is not None:
                    products.append(product)

        return HttpResponse(content=serializers.serialize('json', products), content_type='application/json')
