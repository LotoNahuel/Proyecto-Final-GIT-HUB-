# Generated by Django 4.1.7 on 2023-04-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0012_alter_modelo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
