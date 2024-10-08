from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from management import models
from management.api.user.serializers import (
    CreateElectionSerializer,
    UpdateStatusElectionSerializer,
    GetElectionSerializer
)

@api_view(['POST'])
def create_election(request):
    serializer = CreateElectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': f'Election created successfully from {serializer.data['start_date']} until {serializer.data['end_date']}'},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_elections(request):
    elections = models.Election.objects.all()
    serializer = GetElectionSerializer(elections, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
    return Response(data=msg,status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def insert_candidate(request, election_id, candidate_id):
    election = get_object_or_404(models.Election, election_id=election_id)
    candidate = get_object_or_404(models.Candidate, candidate_id=candidate_id)
    election.candidates.add(candidate)
    election.save()
    response = GetElectionSerializer(election).data
    return Response(data=response,status=status.HTTP_201_CREATED)