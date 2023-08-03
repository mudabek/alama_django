# Generated by Django 4.2.3 on 2023-07-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_course_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
