from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from management import models
from management.models import ElectionStatus, Election, Candidate
from management.serialiazers.serializers import (
    CreateElectionSerializer,
    CandidateRequestSerializer,
    GetElectionSerializer, EndElectionSerializer
)


@api_view(['POST', 'GET'])
def elections(request):
    if request.method == 'POST':
        serializer = CreateElectionSerializer(data=request.data)

        if validate_dates(serializer):
            return Response(
                {
                    'error': 'Já existe uma eleição com esta mesma data.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Valida os dados do serializer
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'msg': 'Eleição criada com sucesso!',
                    'start_date': serializer.data['start_date'],
                    'end_date': serializer.data['end_date'],
                    'status': serializer.data['status']
                },
                status=status.HTTP_201_CREATED
            )

        # Se os dados não forem válidos, retornamos erros mais claros
        return Response(
            {
                'error': 'Error ao tentar criar uma nova eleição.',
                'details': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'GET':
        election = models.Election.objects.all()
        serializer = GetElectionSerializer(election, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def validate_dates(serializer):
    return models.Election.objects.filter(start_date=serializer.initial_data.get('start_date')).exists() or \
        models.Election.objects.filter(end_date=serializer.initial_data.get('end_date')).exists()


@api_view(['GET'])
def get_election_by_id(request, election_id):
    election = get_object_or_404(models.Election, pk=election_id)
    serializer = GetElectionSerializer(election)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_candidate(request, election_id):
    election = get_object_or_404(models.Candidate, candidate_id=election_id)
    election.delete()
    msg = {'msg': f'Eleição {election_id} deletada com sucesso.'}
    return Response(data=msg, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def insert_candidate(request, election_id, user_id):
    user = get_object_or_404(models.User, user_id=user_id)
    election = get_object_or_404(models.Election, election_id=election_id)

    if election.candidates.filter(user=user).exists():
        return Response(
            {
                "error": "Este usuário ja existe nesta eleição.",
                "id": user_id,
                "name": user.name,
            },
            status=status.HTTP_400_BAD_REQUEST)

    candidate_serializer = CandidateRequestSerializer(data=request.data)
    if candidate_serializer.is_valid():
        candidate = candidate_serializer.save(user=user)
        election.candidates.add(candidate)

        election.status = ElectionStatus.IN_PROGRESS.value

        election.save()
        response = GetElectionSerializer(election).data
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(candidate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def finish(request):
    serializer = EndElectionSerializer(data=request.data)
    if serializer.is_valid():
        election = Election.objects.get(election_id=serializer.validated_data['election_id'])

        candidate_votes = {}
        for candidate in election.candidates.all():
            candidate_votes[candidate.candidate_id] = candidate.votes.count()

        winner_id = max(candidate_votes, key=candidate_votes.get)
        winner = Candidate.objects.get(candidate_id=winner_id)

        election.status = ElectionStatus.COMPLETED.value
        election.save()

        return Response(
            {
                'message': 'Eleição encerrada com sucesso.',
                'winner': {
                    'candidate_id': winner.candidate_id,
                    'name': winner.user.name,
                    'vote_count': candidate_votes[winner_id],
                }
            },
            status=status.HTTP_200_OK
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)