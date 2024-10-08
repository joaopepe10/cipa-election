# Generated by Django 5.1.1 on 2024-10-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_alter_election_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
    ]
