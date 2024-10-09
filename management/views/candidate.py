from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from management import models
from management.serialiazers.serializers import (
    CandidateResponseSerializer,
    UpdateSpeechSerializer
)


@api_view(['GET', 'DELETE', 'PUT'])
def candidates(request, candidate_id):
    if request.method == 'GET':
        candidate = get_object_or_404(models.Candidate, candidate_id=candidate_id)
        serializer = CandidateResponseSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        candidate = get_object_or_404(models.Candidate, candidate_id=candidate_id)
        candidate.delete()
        msg = {'msg': f'Candidate {candidate_id} deleted successfully'}
        return Response(data=msg, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        candidate = get_object_or_404(models.Candidate, candidate_id=candidate_id)
        serializer = UpdateSpeechSerializer(candidate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_candidates(request):
    candidate = models.Candidate.objects.all()
    serializer = CandidateResponseSerializer(candidate, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
