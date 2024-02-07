from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image_url = models.CharField(max_length=2000, blank=True, default=False)
    book_available = models.BooleanField(blank=False)
    pdf_files = models.FileField(upload_to='pdf_files/', default=None)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)


class WishListItems(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    