from datetime import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from management import models
from management.models import ElectionStatus
from management.serialiazers.serializers import (
    CreateElectionSerializer,
    CandidateRequestSerializer,
    GetElectionSerializer
)


def result(request):
    return render(request, 'voto/TelaVotacao.html', status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def elections(request):
    if request.method == 'POST':
        serializer = CreateElectionSerializer(data=request.data)

        if validate_dates(serializer):
            return Response(
                {
                    'error': 'An election already exists with the same start or end date. Please choose different dates.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Valida os dados do serializer
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'msg': 'Election created successfully!',
                    'start_date': serializer.data['start_date'],
                    'end_date': serializer.data['end_date'],
                    'status': serializer.data['status']
                },
                status=status.HTTP_201_CREATED
            )

        # Se os dados não forem válidos, retornamos erros mais claros
        return Response(
            {
                'error': 'Error creating the election. Check the data provided.',
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
    msg = {'msg': f'Election {election_id} deleted successfully'}
    return Response(data=msg, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def insert_candidate(request, election_id, user_id):
    user = get_object_or_404(models.User, user_id=user_id)
    election = get_object_or_404(models.Election, election_id=election_id)

    if election.candidates.filter(user=user).exists():
        return Response(
            {
                "error": "This user is already registered for this election.",
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


