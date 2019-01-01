from django.contrib import admin
from .models import Product, Category, User
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'quantity', 'category', 'user']
    list_filter = ['price']


class CategoryAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name']

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['first_name', 'last_name', 'username', 'email', 'position']
    list_filter = ['position']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)

