# Generated by Django 4.2.1 on 2023-06-19 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
