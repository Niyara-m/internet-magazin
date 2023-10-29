from django.contrib import admin
from . models import Category, Products, Cart

admin.site.register(Cart)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'amount')
    list_display_links = ('name',)