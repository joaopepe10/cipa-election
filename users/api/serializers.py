from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'user_id']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = ['user', 'speech']