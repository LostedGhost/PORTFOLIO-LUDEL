# Generated by Django 5.0.6 on 2024-05-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0003_information_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
