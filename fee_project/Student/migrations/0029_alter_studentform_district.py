# Generated by Django 4.2.5 on 2023-09-26 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0005_rename_state_district_state_rename_state_state_state_and_more'),
        ('Student', '0028_alter_studentform_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.district'),
        ),
    ]
