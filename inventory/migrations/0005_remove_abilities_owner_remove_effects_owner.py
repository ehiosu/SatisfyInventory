# Generated by Django 4.1 on 2023-01-04 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_remove_inventoryitem_inventory_inventory_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="abilities",
            name="Owner",
        ),
        migrations.RemoveField(
            model_name="effects",
            name="Owner",
        ),
    ]