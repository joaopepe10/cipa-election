from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from management import models
from management.serialiazers.serializers import VoteSerializer, CreateVoteDto

@api_view(['POST'])
def create_vote(request):

    dto = CreateVoteDto(data=request.data)
    if not dto.is_valid():
        return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)
    election = get_object_or_404(models.Election, pk=dto.validated_data['election_id'])
    candidate = get_object_or_404(models.Candidate, pk=dto.validated_data['candidate_id'])

    vote = models.Vote.objects.create(election=election, candidate=candidate)
    serializer = VoteSerializer(vote)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_vote_by_id(request, id):
    vote = get_object_or_404(models.Vote, pk=id)
    serializer = VoteSerializer(vote)
    return Response(serializer.data, status=status.HTTP_200_OK)
