# Generated by Django 3.1 on 2020-08-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0002_auto_20200825_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_data',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
    ]
