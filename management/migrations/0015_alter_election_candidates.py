# Generated by Django 5.1.1 on 2024-10-08 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_alter_election_end_date_alter_election_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='candidates',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.candidate'),
        ),
    ]