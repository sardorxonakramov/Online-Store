from django.contrib import admin

from .models import Product, Comment, Cart


admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Cart)
