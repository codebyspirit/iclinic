# Generated by Django 4.1 on 2023-03-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0004_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
