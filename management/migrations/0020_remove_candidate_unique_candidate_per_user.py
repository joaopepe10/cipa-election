# Generated by Django 5.1.1 on 2024-10-09 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_alter_election_candidates'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='candidate',
            name='unique_candidate_per_user',
        ),
    ]
