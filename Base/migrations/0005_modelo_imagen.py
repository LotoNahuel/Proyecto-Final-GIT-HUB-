# Generated by Django 4.1.7 on 2023-04-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='post'),
        ),
    ]
