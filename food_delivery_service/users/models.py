from django.db import models
from django.contrib.auth.models import AbstractUser
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
