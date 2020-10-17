from django.db import models
from wholesale.models import Book
# Create your models here.

class Slider(models.Model):
    # TODO: Define fields here
    mainText = models.CharField(blank=True, max_length=100)
    subText = models.CharField(blank=True, max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

class Scroller(models.Model):
    # TODO: Define fields here
    tag = models.CharField(blank=True, max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
