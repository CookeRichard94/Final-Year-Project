from django.urls import path, include

from . import views

urlpatterns = [
    #path('products/<str:product_id>/', views.product_page, name='product_page'),
    path('products', views.ProductList.as_view(), name="index"),

    #path('products/', include('urls.py')),
]
