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
                # product.image = request.POST['image']
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
            #return redirect(product_view, pk=product.pk)
        #return render(request, 'store/product/edit_product.html.jinja2',product)


def view_user(request):
    # user = User.objects.get(username=request.session.username)
    if request.method == "GET":
        if request.GET.get("edit") is not None:
            return render(request, 'customers/edit_user.html.jinja2')
        else:
            return render(request, 'customers/view_user.html.jinja2')
    elif request.method == "POST":
        user = User.objects.get(pk=request.user.pk)
        # if request.POST['username'] == User.objects.get(user.username):
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        # user = authenticate(request, username=username, password=password)
        return redirect(view_user)


def index(request):
    return render(request, 'store/product/list.html.jinja2', {'products': Product.objects.all()})

def about(request):
    return render(request, 'footer/about.html.jinja2')

def terms(request):
    return render(request, 'footer/terms.html.jinja2')

def privacy(request):
    return render(request, 'footer/privacy.html.jinja2')

def authors(request):
    return render(request, 'footer/authors.html.jinja2')


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
        print(request.POST.keys())
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, email=email)
            user.save()
            user = authenticate(request, username=username, password=password)
        else:
            redirect(index)

        if user is not None:
            login(request, user)
            return redirect('view_user')

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
