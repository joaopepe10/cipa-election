from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from management import models
from management.models import Vote
from management.serialiazers.serializers import VoteSerializer, SendVoteCandidateSerializer


@api_view(['POST'])
def post_vote(request):
    if request.method == 'POST':
        dto = SendVoteCandidateSerializer(data=request.data)
        if not dto.is_valid() and Vote.objects.filter(user_id=dto['user'], election_id=dto['election']).exists():
            return Response(
            {
                'error': 'User already voted',
                'details': dto.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

        user = get_object_or_404(models.User, pk=dto.validated_data['user'])
        election = get_object_or_404(models.Election, pk=dto.validated_data['election'])
        candidate = get_object_or_404(models.Candidate, pk=dto.validated_data['candidate'])

        vote = Vote.objects.create(user=user, election=election, candidate=candidate)
        vote.save()
        response = VoteSerializer(vote).data
        return Response(data=response, status=status.HTTP_201_CREATED)


