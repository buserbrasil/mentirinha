import redis


redis_client = redis.Redis(**settings.REDIS_CONNECTION_PARAMS)


def incr(url):
    return redis_client.incr(f'url_{url}')


def list_shortned_urls_ids():
    return redis_client.keys('url_*')


def getdel(url):
    return redis_client.getdel(url)
