# Generated by Django 4.1.1 on 2022-11-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_seccion_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="seccion",
            name="consejo",
            field=models.CharField(max_length=140, null=True),
        ),
    ]
