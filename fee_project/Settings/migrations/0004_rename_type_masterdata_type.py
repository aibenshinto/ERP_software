# Generated by Django 4.2.5 on 2023-09-21 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0003_companies_active_courses_active_state_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterdata',
            old_name='Type',
            new_name='type',
        ),
    ]