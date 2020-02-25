from unittest import loader

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from store.models import Product
from store.forms import ProductForm

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product
    # Field must be same as the model attribute
    fields = ['name', 'price', 'size']
    success_url = reverse_lazy('product_list')

class ProductCreate(CreateView):
    model = Product
    # Field must be same as the model attribute
    fields = ['name', 'price', 'size']
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')