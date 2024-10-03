from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from management import models
from management.api.user.serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = models.User.objects.all()  # Get all objects in User's database (It returns a queryset)

        serializer = UserSerializer(users, many=True)  # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)  # Return the serialized data

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_id(request, id):
    if request.method == 'GET':
        try:
            user = models.User.objects.get(user_id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user(request):
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'User created successfully'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response('Ocorreu um erro', status=status.HTTP_400_BAD_REQUEST)
