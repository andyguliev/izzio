# Generated by Django 2.2.7 on 2020-01-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_remove_good_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='good',
        ),
        migrations.AddField(
            model_name='order',
            name='good',
            field=models.ManyToManyField(to='catalog.Good'),
        ),
    ]
