# Generated by Django 4.1.3 on 2022-12-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctionlisting_krajb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'get_latest_by': 'bids'},
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='krajbiddinga',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
