# Generated by Django 4.1.5 on 2023-01-29 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communicator_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='status',
        ),
    ]
