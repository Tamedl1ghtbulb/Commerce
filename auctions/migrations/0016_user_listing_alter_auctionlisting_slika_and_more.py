# Generated by Django 4.1.4 on 2023-02-02 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_bids_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.auctionlisting'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='slika',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Bookmarks',
        ),
    ]
