import os
from functools import wraps
from django.http import JsonResponse


def require_bearer_token(view_func):
    """
    Decorator to require Bearer token authentication for API views.

    Checks the Authorization header for a Bearer token and validates it
    against the API_TOKEN environment variable.

    Returns 401 if authentication fails.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization', '')

        if not auth_header.startswith('Bearer '):
            return JsonResponse(
                {'error': 'Missing or invalid Authorization header'},
                status=401
            )

        token = auth_header[7:]  # Remove 'Bearer ' prefix
        expected_token = os.getenv('API_TOKEN', '')

        if not expected_token:
            return JsonResponse(
                {'error': 'API authentication not configured'},
                status=500
            )

        if token != expected_token:
            return JsonResponse(
                {'error': 'Invalid authentication token'},
                status=401
            )

        return view_func(request, *args, **kwargs)

    return wrapper
