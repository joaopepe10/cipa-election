# Generated by Django 5.1.1 on 2024-10-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_remove_election_candidates_election_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='candidates',
            field=models.ManyToManyField(to='management.candidate'),
        ),
    ]