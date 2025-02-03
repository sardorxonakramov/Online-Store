from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserModelManager, AdminManager, CustomerManager


class UserModel(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='user-images/',
                                      default='user-images/user-default.png',
                                      null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    objects = UserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.fullname} - {self.email}'


class Admin(UserModel):
    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = False
        self.is_staff = True
        self.is_admin = True
        self.is_superuser = False
        super().save(*args, **kwargs)


class Customer(UserModel):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = True
        self.is_staff = False
        self.is_admin = False
        self.is_superuser = False
        super().save(*args, **kwargs)
