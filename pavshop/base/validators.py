from django.core.exceptions import ValidationError




def validate_gmail(value):
    if not value.endswith('gmail.com'):
        raise ValidationError('Email input must be gmail')
    return True


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 Mib')
