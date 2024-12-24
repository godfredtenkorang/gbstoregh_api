from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from .models import Category, Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def all_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)