# Generated by Django 2.2.7 on 2020-01-11 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20200111_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='good',
        ),
        migrations.AddField(
            model_name='people',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Good'),
        ),
    ]
