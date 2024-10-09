from rest_framework import serializers
from management import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['user_id', 'name', 'email']

class CandidateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = ['speech']

class UpdateSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = ['speech']


class CandidateResponseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = models.Candidate
        fields = ['candidate_id','speech', 'user', 'registration_date']
        def validate(self, data):
            # Verifica se o usuário já tem um candidato
            if models.Candidate.objects.filter(user=data['user']).exists():
                raise serializers.ValidationError("This user already has a candidate.")
            return data

class CreateElectionSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    end_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    class Meta:
        model = models.Election
        fields = ['start_date', 'end_date', 'status']

class GetElectionSerializer(serializers.ModelSerializer):
    candidates = CandidateResponseSerializer(many=True)  # Serializa a lista de candidatos corretamente
    class Meta:
        model = models.Election
        fields = ['election_id','status' ,'candidates', 'start_date', 'end_date']

class UpdateStatusElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Election
        fields = 'status'