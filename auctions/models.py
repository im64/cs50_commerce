from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctioneer")
    name = models.CharField(max_length=128)
    description = models.TextField()
    starting_price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='img')
    is_active = models.BooleanField(default=False)
    

class Bid(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    price = models.IntegerField()


class Comment(models.Model):
    value = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="commented_auction")
