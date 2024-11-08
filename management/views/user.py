from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from management import models
from management.serialiazers.serializers import (
    UserSerializer
)

## RENDERIZAR A TELA DESEJADA COM SEU RESPECTIVO PATH
## ENVIAR

def index(request):
    return render(request, 'home/home.html')

def register_user(request):
    return render(request, 'cadastro/TelaCadastro.html')


@api_view(['POST', 'GET'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'msg': 'User created successfully',
                    'user_id': serializer.data['user_id'],
                    'name': serializer.data['name'],
                    'email': serializer.data['email']
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = get_object_or_404(models.User, user_id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
