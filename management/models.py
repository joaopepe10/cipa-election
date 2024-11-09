from django.db import models
from enum import Enum

from django.utils import timezone
from rest_framework.exceptions import ValidationError


# CRIAR MODELO BANCO DE DADOS
# py manage.py makemigrations

#GERAR DADOS
# py manage.py migrate

#RUN PROJECT
# python manage.py runserver

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    candidate_id = models.IntegerField(null=True, blank=True, db_column='candidate_id')

    def __str__(self):
        return f'user_ id: {self.user_id}, name: {self.name}, email: {self.email}'

# Candidate
class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_user',
        db_column='user_id',
        blank=False
    )
    speech = models.TextField(unique=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    count_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"name: {self.user.name}, speech: {self.speech}, date_apply: {self.registration_date}"

class ElectionStatus(Enum):
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED '

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    candidates = models.ManyToManyField(Candidate)
    status = models.CharField(
        max_length=20,
        choices=ElectionStatus.choices(),
        default=ElectionStatus.NOT_STARTED.value
    )
    start_date = models.DateTimeField(null=False, unique=True)
    end_date = models.DateTimeField(null=False, unique=True)

    def __str__(self):
        return f'Election {self.election_id} - Status: {self.status}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    vote_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'election')

    def clean(self):
        if self.election.status != ElectionStatus.IN_PROGRESS.value:
            raise ValidationError("A eleição não está em progresso, o voto não pode ser registrado.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Vote, self).save(*args, **kwargs)