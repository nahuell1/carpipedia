# Generated by Django 3.2.7 on 2021-10-02 05:03

from django.conf import settings
from django.db import migrations
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount import providers

def cargar_aplicaciones(apps, schema_editor):
    """ Genera la carga inicial de las aplicaciones
    Google y Facebook para poder logearse """
    # Configuro el sitio de django con los valores del virtualhost
    sitio = Site.objects.create(name=settings.VIRTUAL_HOSTNAME, domain=settings.VIRTUAL_HOST)
    facebook = SocialApp.objects.create(
        # Estos datos son los que nos proporciona la aplicación
        provider = "facebook",
        name = "Facebook",
        client_id = "408165317356447",
        secret = "63867a34f3eeb6f704f0978979c5b536",
    )
    facebook.sites.add(sitio)
    facebook.save()
    google = SocialApp.objects.create(
        # Estos datos son los que nos proporciona la aplicación
        provider = "google",
        name = "Google",
        client_id = "129172837043-41it8ebm74u145228cjahhc045jc09eh.apps.googleusercontent.com",
        secret = "PuYKO9yoHz57D6sUVzQSWGd2",
    )
    google.sites.add(sitio)
    google.save()
    


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_aplicaciones),
    ]
