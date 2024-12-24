from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'get_category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'get_image_1', 'get_image_2', 'get_image_3', 'normal_price', 'final_price']
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']