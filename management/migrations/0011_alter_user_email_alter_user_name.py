# Generated by Django 5.1.1 on 2024-10-07 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
