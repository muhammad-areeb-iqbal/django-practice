from django.core.exceptions import ValidationError


def validate_author_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Not a valid email")


def validate_school_email(value):
    if not ".edu" in value:
        raise ValidationError("A valid school email must be entered in")
    else:
        return value