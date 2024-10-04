from rest_framework import serializers
from management import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'user_id']

class CandidateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = ['speech']

class CandidateResponseSerializer(serializers.ModelSerializer):
    # Permitir valores nulos e campos opcionais
    class Meta:
        model = models.Candidate
        fields = ['speech', 'user']