# Generated by Django 5.1.1 on 2024-10-04 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_candidate_registration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
