# Generated by Django 5.1.1 on 2024-10-01 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
