# Generated by Django 5.0.6 on 2024-06-14 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0004_movimentacao_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movimentacao",
            name="data",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 6, 14, 13, 20, 11, 262577, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
