from django.contrib import admin

from . import models
from .models import Book

# Register your models here.

admin.site.register(models.Book)
