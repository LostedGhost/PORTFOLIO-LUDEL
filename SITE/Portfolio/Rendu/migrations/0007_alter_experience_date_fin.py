# Generated by Django 5.0.6 on 2024-05-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0006_information_nom_complet_projet_lien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='date_fin',
            field=models.DateField(null=True),
        ),
    ]
