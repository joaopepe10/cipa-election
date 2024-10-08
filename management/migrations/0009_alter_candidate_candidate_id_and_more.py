# Generated by Django 5.1.1 on 2024-10-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_candidate_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddConstraint(
            model_name='candidate',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_candidate_per_user'),
        ),
    ]