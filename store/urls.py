from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all-products'),
    path('categories/', views.all_categories, name='all-categories'),
    path('categories/<int:pk>/', views.get_category, name='get-category')
]