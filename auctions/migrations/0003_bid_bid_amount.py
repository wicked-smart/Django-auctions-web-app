# Generated by Django 4.1.2 on 2022-10-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing_comment_bid_user_items_bought_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_amount',
            field=models.FloatField(default=None),
        ),
    ]
