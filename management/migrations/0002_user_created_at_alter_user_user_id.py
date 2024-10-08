# Generated by Django 5.1.1 on 2024-09-30 23:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
