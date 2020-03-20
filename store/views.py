from unittest import loader

from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core import serializers
from store.models import Product
from store.forms import ProductForm

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