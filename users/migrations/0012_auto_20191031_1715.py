# Generated by Django 2.2.6 on 2019-10-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191031_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='is_Mentor',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]