# Generated by Django 4.1.4 on 2023-02-03 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_remove_user_listing_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='following',
        ),
        migrations.AddField(
            model_name='following',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wpost', to='auctions.auctionlisting'),
            preserve_default=False,
        ),
    ]