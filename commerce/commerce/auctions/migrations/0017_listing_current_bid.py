# Generated by Django 4.2.1 on 2023-06-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_listing_active_alter_listing_starting_bid_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=10),
        ),
    ]