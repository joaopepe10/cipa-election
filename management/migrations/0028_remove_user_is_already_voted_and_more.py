# Generated by Django 5.1.1 on 2024-10-30 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_user_is_already_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_already_voted',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'election')},
        ),
    ]
