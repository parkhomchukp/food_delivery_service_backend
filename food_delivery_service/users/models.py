from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from location_field.models.plain import PlainLocationField

from .validators import is_adult_validator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    birthdate = models.DateField(validators=[is_adult_validator])

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthdate']


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    is_vip = models.BooleanField(default=False)
