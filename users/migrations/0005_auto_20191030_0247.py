# Generated by Django 2.2.6 on 2019-10-30 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191030_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workers',
            old_name='profile',
            new_name='user',
        ),
    ]