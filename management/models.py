from django.db import models
from enum import Enum

from django.utils import timezone

# CRIAR MODELO BANCO DE DADOS
# py manage.py makemigrations

#GERAR DADOS
# py manage.py migrate

#RUN PROJECT
# python manage.py runserver

class User(models.Model):
    user_id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, default='', blank=False)
    email = models.CharField(max_length=50, default='', unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    candidate_id = models.IntegerField(null=True, blank=True, db_column='candidate_id')

    def __str__(self):
        return f'user_ id: {self.user_id}, name: {self.name}, email: {self.email}'

# Candidate
class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)  # Mude para AutoField
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_user',
        db_column='user_id',
        blank=False
    )
    speech = models.TextField(unique=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_candidate_per_user')  # Adiciona a restrição
        ]
    def __str__(self):
        return f"Nome Candidato: {self.user.name}, Discurso: {self.speech}, Data inscricao: {self.registration_date}"

class ElectionStatus(Enum):
    NOT_STARTED = 'registered'
    IN_PROGRESS = 'in_voting'
    COMPLETED = 'closed '

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Election(models.Model):
    election_id = models.IntegerField(primary_key=True, editable=False)
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
