# Generated by Django 4.1 on 2023-01-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
