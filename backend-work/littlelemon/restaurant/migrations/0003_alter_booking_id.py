# Generated by Django 4.1.7 on 2023-03-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
