from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.choices import Sex
from core.models import BaseModel


class User(AbstractUser, BaseModel):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+99999999999'. Up to 11 digits allowed.")

    # image = models.ImageField(upload_to='users_images/', default='users_images/default.png')
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.MALE)
    birthday = models.DateField(blank=True, null=True)
    mobile_phone = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
