from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.api_endpoint ),
    path('products/<int:pk>/', views.api_endpoint)
]