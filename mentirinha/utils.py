import random
import string
from mentirinha.models import ShortenedUrl


def generate_short_code(length=6):
    """
    Generate a random short code that doesn't already exist in the database.

    Args:
        length: Length of the short code (default: 6)

    Returns:
        A unique short code string
    """
    characters = string.ascii_letters + string.digits
    max_attempts = 100

    for _ in range(max_attempts):
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if not ShortenedUrl.objects.filter(short_code=short_code).exists():
            return short_code

    # If we couldn't find a unique code in max_attempts, try with longer length
    return generate_short_code(length + 1)
