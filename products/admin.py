from django.contrib import admin
from products.models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","product_name","brand","price"]
