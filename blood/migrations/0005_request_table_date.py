# Generated by Django 3.2.21 on 2024-01-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_auto_20240112_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_table',
            name='date',
            field=models.DateField(default='2024-01-12'),
            preserve_default=False,
        ),
    ]