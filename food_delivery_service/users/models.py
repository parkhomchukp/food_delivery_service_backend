from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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

    class CitiesChoices(models.TextChoices):
        KYIV = 'KV', 'Kyiv'
        LVIV = 'LV', 'Lviv'
        ODESA = 'OD', 'Odesa'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=2, choices=CitiesChoices.choices, default=CitiesChoices.LVIV)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.user
