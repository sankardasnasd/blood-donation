# Generated by Django 4.2.5 on 2024-03-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0011_alter_complaint_table_date_alter_feedback_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_bank_table',
            name='phonno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blood_bank_table',
            name='pin',
            field=models.CharField(max_length=100),
        ),
    ]
