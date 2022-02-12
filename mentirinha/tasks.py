from django.db.models import F, Value
from django.db.models.functions import Coalesce
from mentirinha import counter
from mentirinha.models import ShortenedUrl


def consume_counter():
    for url_id in counter.list_shortened_urls_ids():
        count = counter.getdel(url_id)
        ShortenedUrl.objects.filter(pk=url_id).update(accesses=Coalesce(F('accesses'), Value(0)) + count)
