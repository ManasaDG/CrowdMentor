# Generated by Django 2.2.6 on 2019-10-30 02:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20191030_0253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workers',
            new_name='Worker',
        ),
    ]