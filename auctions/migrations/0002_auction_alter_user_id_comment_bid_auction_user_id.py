# Generated by Django 4.0.1 on 2022-10-06 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('descripton', models.TextField()),
                ('photo', models.BinaryField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_auction', to='auctions.auction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctions.auction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctioneer', to=settings.AUTH_USER_MODEL),
        ),
    ]