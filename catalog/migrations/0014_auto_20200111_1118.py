# Generated by Django 2.2.7 on 2020-01-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20200111_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='people',
        ),
        migrations.AddField(
            model_name='people',
            name='good',
            field=models.ManyToManyField(to='catalog.Good'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
