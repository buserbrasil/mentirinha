import json
from django.http import JsonResponse
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from mentirinha.models import ShortenedUrl
from mentirinha import counter
from mentirinha.auth import require_bearer_token
from mentirinha.utils import generate_short_code
from sample_project.settings import BASE_URL


def list_all(request):
    response = {
        'shortened_urls': [str(url) for url in ShortenedUrl.objects.all()]
    }

    return JsonResponse(response)


def redirect_to(request, short_code=None):
    shortened_url = get_object_or_404(ShortenedUrl, short_code=short_code)
    counter.incr(shortened_url.id)
    return redirect(shortened_url.original_url)


def ping(request):
    return JsonResponse({"pong": True})


@csrf_exempt
@require_bearer_token
def shorten_url(request):
    """
    API endpoint to create shortened URLs.

    Accepts POST requests with JSON body:
    {
        "url": "https://example.com/long-url",
        "short_code": "optional-custom-code"  # optional
    }

    Returns:
    {
        "short_url": "http://localhost:8000/abc123",
        "short_code": "abc123"
    }

    Requires Bearer token authentication via Authorization header.
    """
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Only POST method is allowed'},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON in request body'},
            status=400
        )

    original_url = data.get('url')
    if not original_url:
        return JsonResponse(
            {'error': 'Missing required field: url'},
            status=400
        )

    # Get custom short_code or generate one
    short_code = data.get('short_code')
    if short_code:
        # Validate that custom short_code is not already in use
        if ShortenedUrl.objects.filter(short_code=short_code).exists():
            return JsonResponse(
                {'error': f'Short code "{short_code}" is already in use'},
                status=409
            )
    else:
        short_code = generate_short_code()

    # Create the shortened URL
    shortened_url = ShortenedUrl(
        short_code=short_code,
        original_url=original_url
    )

    try:
        shortened_url.full_clean()
        shortened_url.save()
    except ValidationError as e:
        return JsonResponse(
            {'error': str(e.message_dict)},
            status=400
        )

    return JsonResponse({
        'short_url': f'{BASE_URL}/{short_code}',
        'short_code': short_code
    }, status=201)
