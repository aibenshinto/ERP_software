# Generated by Django 4.2.5 on 2023-09-13 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='payment_mode',
        ),
    ]
