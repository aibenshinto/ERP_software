# Generated by Django 4.2.5 on 2023-09-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0026_rename_receipt_number_receipts_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='payment_type',
            field=models.CharField(choices=[('One Time', 'One Time '), ('Two Time', 'Two Time '), ('Three Time', 'Three Time')], max_length=20, verbose_name='Installment Type'),
        ),
    ]
