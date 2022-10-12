from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models





class Category(models.Model):
    category_name = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.category_name}"



class Listing(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.FileField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")
    starting_bid = models.IntegerField()
    current_bid = models.IntegerField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, related_name="watchers")
    items_bought = models.ManyToManyField(Listing, blank=True, related_name="buyers")
    listing = models.ManyToManyField(Listing, blank=True, related_name="listers")

    def __str__(self):
        return f"{self.username}"


class Bid(models.Model):
    listing = models.ManyToManyField(Listing, related_name="bids")
    bid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_at = models.DateTimeField(auto_now_add=True)
    bid_amount = models.FloatField(default=None)


class Comment(models.Model):
    listing = models.ManyToManyField(Listing, related_name="comments")
    comment_text = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
