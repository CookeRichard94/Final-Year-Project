import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from store.models import Product


# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product
    # Field must be same as the model attribute
    fields = ['name', 'price', 'size', 'quantity']
    success_url = reverse_lazy('product_list')

class ProductCreate(CreateView):
    model = Product
    # Field must be same as the model attribute
    fields = ['name', 'price', 'size', 'quantity']
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


def index(request):
    context = {'products': Product.objects.all()}
    if 'username' in request.session:
        context['user'] = User.objects.get_by_natural_key(request.session['username'])

    return render(request, 'store/product_list.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('product_list')

        else:
            return redirect('login')

    elif request.method == 'GET':
        return render(request, 'registration/login.html')

def cart(request):
    if request.method== 'POST':
        action = request.POST.get("action", None)
        if action == "add_to_cart" or action == "remove_from_cart":
            product_id=request.POST.get("product_id", None)
            if product_id is not None and product_id.isnumeric():
                product = Product.objects.get(pk=product_id)
                if product is not None:
                    cart = str(request.session.get("cart", "")).split(",")
                    cart.append(product_id) if action == "add_to_cart" else cart.remove(product_id)
                    request.session["cart"] = ",".join([i for i in cart if i != ""])
                    return HttpResponse(status=200)
                else:
                    return HttpResponse(status=404)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(content="unknown action", status=400)
    elif request.method=='GET':
        context = {}
        if 'username' in request.session:
            context['user'] = User.objects.get_by_natural_key(request.session['username'])

        cart = str(request.session.get("cart", "")).split(",")
        context["cart"] = []
        for product_id in cart:
            if not product_id.isnumeric():
                continue
            product = Product.objects.get(pk=product_id)
            if product is not None:
                context["cart"].append(product)
        products = [Product.objects.get(id=pk) for pk in cart]
        return HttpResponse(content = serializers.serialize('json', products),content_type='application/json')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #User.objects.create_user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('product_list')

        else:
            return redirect('login')

    elif request.method == 'GET':
        return render(request, 'registration/register.html', {})

def logout(request, context=None):
    if request.method == 'POST':
        request.session.clear()
        return redirect('product_list')


    elif request.method == 'GET':
        return render(request, 'store/product_list.html', {})