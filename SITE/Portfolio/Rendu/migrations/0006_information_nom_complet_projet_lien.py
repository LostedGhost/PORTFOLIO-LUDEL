# Generated by Django 5.0.6 on 2024-05-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0005_information_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='nom_complet',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='projet',
            name='lien',
            field=models.CharField(default='#', max_length=200),
        ),
    ]