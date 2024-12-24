from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register(request):
    serialiser = RegisterSerializer(data=request.data)
    if serialiser.is_valid():
        user = serialiser.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User registed successfully",
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successfully",
            "token": token.key
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)