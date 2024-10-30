from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from management import models
from management.models import Vote, Election, ElectionStatus


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
        fields = ['candidate_id','speech', 'user', 'registration_date', 'count_votes']
        def validate(self, data):
            if models.Candidate.objects.filter(user=data['user']).exists():
                raise serializers.ValidationError("This user already has a candidate.")
            return data

class CreateElectionSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    end_date = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    class Meta:
        model = models.Election
        fields = ['start_date', 'end_date', 'status']

class EndElectionSerializer(serializers.Serializer):
    election_id = serializers.IntegerField()

    def validate_election_id(self, value):
        election = Election.objects.filter(election_id=value).first()
        if not election:
            raise serializers.ValidationError("Eleição não encontrada.")
        if election.status != ElectionStatus.IN_PROGRESS.value:
            raise serializers.ValidationError("A eleição não está em andamento.")
        return value

class GetElectionSerializer(serializers.ModelSerializer):
    candidates = CandidateResponseSerializer(many=True)
    class Meta:
        model = models.Election
        fields = ['election_id','status' ,'candidates', 'start_date', 'end_date']

class UpdateStatusElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Election
        fields = 'status'

class SendVoteCandidateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    election = serializers.IntegerField()
    candidate = serializers.IntegerField()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = ['id', 'user', 'election', 'candidate', 'vote_date']
