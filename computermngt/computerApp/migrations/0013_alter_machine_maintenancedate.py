# Generated by Django 4.1.7 on 2023-05-09 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0012_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 9, 12, 24, 0, 124720)
            ),
        ),
    ]
