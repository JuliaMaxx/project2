# Generated by Django 4.2.1 on 2023-06-07 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_listing_current_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='current_bid',
        ),
    ]
