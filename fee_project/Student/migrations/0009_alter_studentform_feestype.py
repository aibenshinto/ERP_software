# Generated by Django 4.2.5 on 2023-09-21 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0004_rename_type_masterdata_type'),
        ('Student', '0008_alter_studentform_feestype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='feestype',
            field=models.ForeignKey(limit_choices_to={'type': 'Fee Type'}, on_delete=django.db.models.deletion.CASCADE, related_name='FeeStudents', to='Settings.masterdata', verbose_name='Installment Type'),
        ),
    ]
