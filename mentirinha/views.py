from django.http import JsonResponse
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect
from mentirinha.models import ShortenedUrl
from mentirinha import counter


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
