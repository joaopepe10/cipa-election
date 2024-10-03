# Generated by Django 5.1.1 on 2024-10-02 23:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_user_candidate_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('speech', models.TextField(db_column='discurso')),
                ('registration_date', models.DateTimeField(db_column='data_inscricao', default=django.utils.timezone.now)),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='candidate_user', to='management.user')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('candidates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.candidate')),
            ],
        ),
    ]
