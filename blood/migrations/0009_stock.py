# Generated by Django 4.2.5 on 2024-03-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0008_remove_hospital_table_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=300)),
                ('BANK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.blood_bank_table')),
                ('BLOOD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.blood_table')),
            ],
        ),
    ]
