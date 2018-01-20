from django.core.exceptions import ValidationError

def validiate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("We do not accept edu emails")

CATEGORIES = ['Mexican', 'Asian', 'American']

def validate_category(value):
    if not value in CATEGORIES and not value.capitalize() in CATEGORIES:
        raise ValidationError("{value} is not a valid category.".format(value=value))
