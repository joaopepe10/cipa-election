from django.db import models

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

    def __str__(self):
        return f'user_ id: {self.user_id}, name: {self.name}, email: {self.email}'