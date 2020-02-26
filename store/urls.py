from django.urls import path, include

from . import views
from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    #path('products/<str:product_id>/', views.product_page, name='product_page'),
    path('products', views.ProductList.as_view(), name="index"),

    #path('products/', include('urls.py')),

    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]
