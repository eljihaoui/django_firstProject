# Generated by Django 3.2.5 on 2021-07-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
    ]
