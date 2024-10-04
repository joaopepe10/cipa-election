from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from management import models
from management.api.user.serializers import UserSerializer, CandidateRequestSerializer, CandidateResponseSerializer


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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
                return Response(f"User with id not found {id}", status=status.HTTP_404_NOT_FOUND)

            serializer = CandidateRequestSerializer(data=request.data)
            if serializer.is_valid():
                # Cria o candidato com os dados validados e o user
                candidate = serializer.save(user=user)
                candidate_response = CandidateResponseSerializer(candidate)
                return Response(candidate_response.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.User.DoesNotExist:
            return Response(f"User with id {id} not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response('Ocorreu um erro', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_candidates(request):
        if request.method == 'GET':
        # Retorna todos os candidatos
            candidates = models.Candidate.objects.all()

        # Serializa a lista de candidatos com `many=True`
            serializer = CandidateResponseSerializer(candidates, many=True)

        # Retorna os dados serializados
            return Response(serializer.data)