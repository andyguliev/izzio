# Generated by Django 2.2.7 on 2020-01-11 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='people',
        ),
    ]