# Generated by Django 4.2.5 on 2023-09-22 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_alter_studentform_feestype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='student_form',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
    ]
