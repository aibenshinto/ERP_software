# Generated by Django 4.2.5 on 2023-09-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=250)),
                ('Address1', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Website', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'A. Company',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=250)),
                ('Coursecode', models.CharField(max_length=250)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'F.  Course',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualificationname', models.CharField(max_length=250)),
                ('Active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'E. Qualification',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'B. State',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=250)),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.state')),
            ],
            options={
                'verbose_name_plural': 'C. District',
            },
        ),
    ]
