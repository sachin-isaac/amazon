# Generated by Django 4.1 on 2023-04-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_orders_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Out For Shipping", "Out For Shipping"),
                    ("Completed", "Completed"),
                    ("Cancel", "Cancelled"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
    ]
