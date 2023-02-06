# Generated by Django 4.1.4 on 2023-02-03 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_nesto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nesto',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='follower',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
