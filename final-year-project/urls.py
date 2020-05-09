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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from store import views
from store.views import *

urlpatterns = [
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('', index, name='list'),
    path('cart', cart, name='cart'),

    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('products/<int:pk>', product_view, name="product_view"),
    path('profile/', view_user, name="view_user"),
    path('add_product', add_product, name='add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
