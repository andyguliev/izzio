# Generated by Django 2.2.7 on 2020-01-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200111_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='good',
        ),
    ]