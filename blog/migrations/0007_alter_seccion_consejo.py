# Generated by Django 4.1.1 on 2022-11-04 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_seccion_consejo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seccion",
            name="consejo",
            field=models.CharField(max_length=140),
        ),
    ]