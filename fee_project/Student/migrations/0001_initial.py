# Generated by Django 4.2.5 on 2023-09-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('payment_mode', models.CharField(choices=[('full_payment', 'Full Payment'), ('two_time_payment', '2 Time Payment'), ('three_time_payment', '3 Time Payment')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.companies')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.courses')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.district')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.qualification')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Settings.state')),
            ],
            options={
                'verbose_name_plural': 'Student Forms',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('student_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.studentform')),
            ],
            options={
                'verbose_name_plural': 'Receipts',
            },
        ),
    ]
