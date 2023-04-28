# Generated by Django 4.1.7 on 2023-04-27 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0009_remove_modelo_emailusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
    ]
