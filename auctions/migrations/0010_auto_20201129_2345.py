# Generated by Django 3.0.6 on 2020-11-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201128_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='URL_image',
            field=models.CharField(blank=True, help_text='Url of image that going to be displayed on your listing', max_length=2000),
        ),
    ]
