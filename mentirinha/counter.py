import redis
from django.conf import settings

redis_client = redis.Redis(**settings.REDIS_CONNECTION_PARAMS)


def incr(url):
    return redis_client.incr(f'{settings.REDIS_COUNTER_PREFIX}_{url}')


def list_shortened_urls_ids():
    for key in redis_client.keys(f'{settings.REDIS_COUNTER_PREFIX}_*'):
        yield key[len(settings.REDIS_COUNTER_PREFIX) + 1:]


def getdel(url_id):
    key = f'{settings.REDIS_COUNTER_PREFIX}_{url_id}'
    pipeline = redis_client.pipeline(transaction=True)
    pipeline.get(key)
    pipeline.delete(key)
    count, a = pipeline.execute()
    return count

# re-export
lock = redis_client.lock
