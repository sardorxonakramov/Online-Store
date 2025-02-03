from django.contrib import admin
from django.contrib.auth.models import Group

from .models import UserModel, Customer, Admin


admin.site.unregister(Group)
admin.site.register(UserModel)
admin.site.register(Customer)
admin.site.register(Admin)
