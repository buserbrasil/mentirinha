from django.test import TestCase

from mentirinha.models import ShortenedUrl


class TestMentirinha(TestCase):
    fixtures = ["urls.json", ]

    def setUp(self):
        self.url = ShortenedUrl.objects.get(pk=1)

    def test_existing_short_code_should_redirect_with_302(self):
        short_code = self.url.short_code
        r = self.client.get(f'/{short_code}')
        self.assertEqual(302, r.status_code)

    def test_root_should_redirect_without_short_code_with_302(self):
        r = self.client.get('/')
        self.assertEqual(302, r.status_code)

    def test_inexisting_short_code_should_respond_with_404(self):
        short_code = 'idontexist'
        r = self.client.get(f'/{short_code}')
        self.assertEqual(404, r.status_code)

    def test_accesses_counter(self):
        short_code = self.url.short_code
        self.client.get(f'/{short_code}')
        self.url.refresh_from_db()
        self.assertEqual(1, self.url.accesses)
