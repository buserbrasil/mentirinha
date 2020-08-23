from django.test import TestCase, Client

from mentirinha.models import ShortenedUrl


class TestMentirinha(TestCase):
    fixtures = ["urls.json", ]

    def setUp(self):
        self.url = ShortenedUrl.objects.get(pk=1)
        self.client = Client()

    def test_existing_short_code_should_redirect_with_302(self):
        short_code = self.url.short_code
        r = self.client.get(f'/{short_code}')
        self.assertEqual(302, r.status_code)

    def test_inexisting_short_code_should_respond_with_404(self):
        short_code = 'idontexist'
        r = self.client.get(f'/{short_code}')
        self.assertEqual(404, r.status_code)
