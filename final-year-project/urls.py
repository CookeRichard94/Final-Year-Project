"""final-year-project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from store import views
from store.views import index

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('', index, name='product_list'),
    path('cart', views.cart, name='cart'),

    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
]
