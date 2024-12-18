from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from management import models
from management.serialiazers.serializers import (
    CandidateResponseSerializer,
    UpdateSpeechSerializer
)
from django.shortcuts import render

def register_candidate(request):
    return render(request, 'cadastro/TelaCadastroCandidato.html')

class CandidateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Candidate.objects.all()
    lookup_field = 'candidate_id'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateSpeechSerializer
        return CandidateResponseSerializer

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response({'msg': f"Candidato {kwargs['candidate_id']} deletado com sucesso"}, status=status.HTTP_200_OK)

class CandidateListView(ListAPIView):
    queryset = models.Candidate.objects.all()
    serializer_class = CandidateResponseSerializer

class CandidateRegisterView(CreateAPIView):
    queryset = models.Candidate.objects.all()
    serializer_class = CandidateResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = CandidateResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': f"Candidate {serializer.data['candidate_id']} created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

