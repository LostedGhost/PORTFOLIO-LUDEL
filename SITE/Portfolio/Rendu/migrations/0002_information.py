# Generated by Django 5.0.6 on 2024-05-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=255)),
                ('prenom', models.CharField(blank=True, max_length=255)),
                ('profil', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=255)),
                ('a_propos', models.TextField(blank=True)),
                ('localisation', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
