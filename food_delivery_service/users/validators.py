from django.core.exceptions import ValidationError
from datetime import date


def is_adult_validator(value: date):
    if value.year > (date.today().year - 18):
        raise ValidationError('You should be at least 18 years old')
