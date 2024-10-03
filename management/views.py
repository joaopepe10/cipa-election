from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from management import models
from management.api.user.serializers import UserSerializer, CandidateSerializer


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
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


@api_view(['POST'])
def user(request):
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'User created successfully'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response('Ocorreu um erro', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def apply_candidate(request, id):
    if request.method == 'POST':
        try:
            user = models.User.objects.get(user_id=id)
            if user is None:
                return Response(f"User with id not found {id}",status=status.HTTP_404_NOT_FOUND)
            new_candidate = request.data
            new_candidate['user'] = user
            new_candidate['user_id'] = id
            serializer = CandidateSerializer(data=new_candidate)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    return Response('Ocorreu um erro', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_candidates(request):
    if request.method == 'GET':
        candidates = models.Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)