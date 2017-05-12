from django.test import TestCase, Client

from django.urls import reverse_lazy

from tournament.models import Tournament


class IndexViewTests(TestCase):

    def setUp(self):
        self.url = reverse_lazy('tournament:index')
        self.client = Client()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
