# Generated by Django 3.2.21 on 2024-01-12 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_blood_bank_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_bank_table',
            name='HOSPITAL',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blood.hospital_table'),
            preserve_default=False,
        ),
    ]
