# Generated by Django 4.1 on 2023-01-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_abilities_level_abilities_owner_effects_level_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="abilities",
            name="AbilityID",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="effects",
            name="AbilityID",
            field=models.PositiveIntegerField(default=1),
        ),
    ]