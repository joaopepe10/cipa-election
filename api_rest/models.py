from django.db import models

# CRIAR MODELO BANCO DE DADOS
# py manage.py makemigrations

#GERAR DADOS
# py manage.py migrate

class User(models.Model):

    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'user_id: {self.user_id}, name: {self.name}, email: {self.email}'