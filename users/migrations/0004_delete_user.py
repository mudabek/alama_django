# Generated by Django 4.2.3 on 2023-07-29 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_profile_courses_purchased_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]