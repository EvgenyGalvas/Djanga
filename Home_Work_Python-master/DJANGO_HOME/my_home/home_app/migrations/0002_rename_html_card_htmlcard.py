# Generated by Django 4.2.1 on 2023-06-05 07:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Html_Card',
            new_name='HtmlCard',
        ),
    ]