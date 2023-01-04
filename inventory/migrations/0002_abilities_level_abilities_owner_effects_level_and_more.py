# Generated by Django 4.1 on 2023-01-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="abilities",
            name="Level",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="abilities",
            name="Owner",
            field=models.TextField(default="Test", max_length=1000),
        ),
        migrations.AddField(
            model_name="effects",
            name="Level",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="effects",
            name="Owner",
            field=models.TextField(default="Test", max_length=1000),
        ),
    ]
