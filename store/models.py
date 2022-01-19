from turtle import color
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


# class Color(models.Model):
#     label = models.CharField(max_length=255)


# class ItemColor(models.Model):
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()

#     def __str__(self) -> str:
#         return self.color

#     class Meta:
#         ordering = ['color']
    




class Product(models.Model):
    UKSIZE8 = '8'
    UKSIZE10 = '10'
    UKSIZE12 = '12'
    UKSIZE14 = '14'
    UKSIZE16 = '18'

    SIZE_CHOICES = [
        (UKSIZE8, 'SIZE 8'),
        (UKSIZE10, 'SIZE 10'),
        (UKSIZE12, 'SIZE 12'),
        (UKSIZE14, 'SIZE 14'),
        (UKSIZE16, 'SIZE 16'),
    ]

    BLUE = 'BLU'
    BLACK = 'BLK'
    RED = 'RED'
    GOLDEN = 'GLD'
    SILVER = 'SIL'
    

    COLOR_CHOICES = [
        (BLUE, 'BLUE'),
        (BLACK, 'BLACK'),
        (RED, 'RED'),
        (GOLDEN, 'GOLD'),
        (SILVER, 'SILVER'),
    ]


    title = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    inventory = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=UKSIZE8)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default=RED)
    # colors = models.ManyToManyField(ItemColor, primary_key=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

