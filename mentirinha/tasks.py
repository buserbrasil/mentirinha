from mentirinha import counter

# TODO: vai ser uma periodic task isso aqui
def consume_counter():
    for url_id in counter.list_shortned_urls_ids():
        counter = counter.getdel(url_id)
        ShortenedUrl.objects.filter(pk=url_id).update(counter=F('counter') + 1)
