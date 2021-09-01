from django.test import TestCase, Client

from mentirinha.models import ShortenedUrl
from mentirinha import tasks, counter


class TestMentirinha(TestCase):
    fixtures = ["urls.json", ]

    def setUp(self):
        self.url = ShortenedUrl.objects.get(pk=1)
        self.client = Client()

    def tearDown(self):
        # flush all pending urls
        for url_id in counter.list_shortened_urls_ids():
            counter.getdel(url_id)
        
        # reset url counter
        self.url.accesses = 0
        self.url.save()

    def test_existing_short_code_should_redirect_with_302(self):
        short_code = self.url.short_code
        r = self.client.get(f'/{short_code}')
        self.assertEqual(302, r.status_code)

    def test_existing_short_code_should_increment_counter(self):
        number_of_access = 3

        for _ in range(number_of_access):
            self.client.get(f'/{self.url.short_code}')

        tasks.consume_counter()
        self.url.refresh_from_db()
        self.assertEqual(self.url.accesses, number_of_access)

    def test_root_should_redirect_without_short_code_with_302(self):
        r = self.client.get('/')
        self.assertEqual(302, r.status_code)

    def test_inexisting_short_code_should_respond_with_404(self):
        short_code = 'idontexist'
        r = self.client.get(f'/{short_code}')
        self.assertEqual(404, r.status_code)
