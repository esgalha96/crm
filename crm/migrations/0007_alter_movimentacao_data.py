# Generated by Django 5.0.6 on 2024-06-14 13:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0006_alter_movimentacao_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movimentacao",
            name="data",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
