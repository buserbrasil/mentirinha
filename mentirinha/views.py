from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from mentirinha.models import ShortenedUrl


def list_all(request):
    response = {
        'shortened_urls': [str(url) for url in ShortenedUrl.objects.all()]
    }

    return JsonResponse(response)


def redirect_to(request, short_code):
    shortened_url = get_object_or_404(ShortenedUrl, short_code=short_code)
    shortened_url.accesses += 1
    shortened_url.save()
    return redirect(shortened_url.original_url)
