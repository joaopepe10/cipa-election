from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from management import models
from management.api.user.serializers import (
    CandidateRequestSerializer,
    CandidateResponseSerializer
)


@api_view(['POST'])
def apply_candidate(request, id):
    user = get_object_or_404(models.User, user_id=id)
    serializer = CandidateRequestSerializer(data=request.data)
    if serializer.is_valid():
        candidate = serializer.save(user=user)
        candidate_response = CandidateResponseSerializer(candidate)
        return Response(candidate_response.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_candidates(request):
    candidates = models.Candidate.objects.all()
    serializer = CandidateResponseSerializer(candidates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_candidate(request,candidate_id):
    candidate = get_object_or_404(models.Candidate, candidate_id=candidate_id)
    candidate.delete()
    msg = {'msg': f'Candidate {candidate_id} deleted successfully'}
    return Response(data=msg,status=status.HTTP_204_NO_CONTENT)