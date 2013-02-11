from tornado.testing import AsyncHTTPTestCase
from app import Application


class HomeTest(AsyncHTTPTestCase):
    def get_app(self):
        return Application()

    def test_homepage_contains_palette(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()

        self.assertIn('Palette', response.body)
