from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.all_categories, name='all-categories'),
    path('categories/<int:pk>/', views.get_category, name='get-category')
]