# Generated by Django 4.2.1 on 2023-06-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_category_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
