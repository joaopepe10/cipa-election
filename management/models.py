from django.db import models
from django.utils import timezone

# CRIAR MODELO BANCO DE DADOS
# py manage.py makemigrations

#GERAR DADOS
# py manage.py migrate

#RUN PROJECT
# python manage.py runserver

class User(models.Model):
    user_id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    candidate_id = models.IntegerField(null=True, blank=True, db_column='candidate_id')

    def __str__(self):
        return f'user_ id: {self.user_id}, name: {self.name}, email: {self.email}'

# Candidate
class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate_user', db_column='user_id')
    speech = models.TextField(db_column='discurso')
    registration_date = models.DateTimeField(default=timezone.now, db_column='data_inscricao')

    def __str__(self):
        return f"Candidate {self.user.name}"

class Election(models.Model):
    election_id = models.IntegerField(primary_key=True, editable=False)
    candidates = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"Election id: {self.election_id}"
