# Generated by Django 4.1.3 on 2022-12-04 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_komentar_klisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apovezano', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
