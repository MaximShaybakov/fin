from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts', 'password']
    list_filter = ['email']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state']
    list_filter = ['name']


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone']
    list_filter = ['city']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordered_items', 'state', 'dt', 'contact']
    list_filter = ['ordered_items', 'state', 'dt']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_info', 'quantity', 'order']
    list_filter = ['product_info', 'quantity', 'order']


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'product', 'shop', 'quantity', 'price', 'price_rrc', 'product_parameters']
    list_filter = ['model', 'product', 'shop']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
