# Generated by Django 4.1.7 on 2023-03-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="will_be_available_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
