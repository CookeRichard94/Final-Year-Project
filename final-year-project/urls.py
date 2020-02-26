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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', views.ProductList.as_view(), name='product_list'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
]

from django.urls import path
from django.contrib import admin

# Use include() to add URLS from the catalog application and authentication system
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls')),
]