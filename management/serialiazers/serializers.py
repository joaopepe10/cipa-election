from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from management import models
from management.models import Vote, Election


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
