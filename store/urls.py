from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    #path('products/<str:product_id>/', views.product_page, name='product_page'),
    path('products', views.ProductList.as_view(), name="index"),
    path('', RedirectView.as_view(url='store/', permanent=True)),
    path('store/', include('store.urls')),
]
