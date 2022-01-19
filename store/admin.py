from django.contrib import admin, messages
from django.db.models.aggregates import Count
from . import models
from store.models import Category, Product

# Register your models here.




@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    list_per_page = 10
    search_fields = ['title']



admin.site.register(Category)
