# Generated by Django 3.2.8 on 2021-10-09 03:31

from django.conf import settings
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_propietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='posts.Categoria'),
        ),
    ]
