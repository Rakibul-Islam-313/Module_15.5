# Generated by Django 4.2.7 on 2023-12-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
