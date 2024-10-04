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
    user = UserSerializer(read_only=True)
    class Meta:
        model = models.Candidate
        fields = ['candidate_id','speech', 'user', 'registration_date']
        def clean(self, value):
         if models.Candidate.objects.filter(user=value).exists():
            raise serializers.ValidationError("Este usuário já possui um candidato.")
         return value