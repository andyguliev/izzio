# Generated by Django 2.2.7 on 2020-01-11 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20200111_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='people',
        ),
    ]
