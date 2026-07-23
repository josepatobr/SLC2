from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.product_home, name=("product_home")),
    path('product_inf/{product.id}', views.product_view, name=("product_view")),
]
