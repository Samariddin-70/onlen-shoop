from django.contrib import admin

from cors.models.products import Category, Product,Cart,Brand


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','deleted']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','ctg','brand']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product','user','total_price']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','icon']