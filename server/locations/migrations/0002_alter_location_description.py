# Generated by Django 4.1.1 on 2022-12-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="description",
            field=models.CharField(max_length=200),
        ),
    ]
