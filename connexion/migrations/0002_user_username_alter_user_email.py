# Generated by Django 4.1 on 2023-03-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]