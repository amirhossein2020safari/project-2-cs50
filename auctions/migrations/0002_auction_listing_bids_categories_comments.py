# Generated by Django 3.0.6 on 2020-10-25 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Auction_listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_title', models.CharField(help_text='This title going to be shown in head of your listing', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('description', models.CharField(help_text='Give more information about your comodity to sell it faster!', max_length=2000)),
                ('starting_price', models.DecimalField(decimal_places=2, help_text='Enter base price of your commodity', max_digits=9)),
                ('URL_image', models.CharField(blank=True, help_text='Url of image that going to be displayed on your listing', max_length=2000)),
                ('bids', models.ManyToManyField(to='auctions.Bids')),
                ('category', models.ForeignKey(blank=True, help_text='Write categoty of your listing', on_delete=django.db.models.deletion.CASCADE, to='auctions.Categories')),
                ('comments', models.ManyToManyField(to='auctions.Comments')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
