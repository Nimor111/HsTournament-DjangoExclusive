from django.test import TestCase, Client

from django.urls import reverse_lazy

from tournament.models import Tournament

from tournament.factories import TournamentFactory, DeckFactory, PlayerFactory, UserFactory
from faker import Factory

faker = Factory.create()


class IndexViewTests(TestCase):

    def setUp(self):
        self.url = reverse_lazy('tournament:index')
        self.client = Client()
        self.tournament = TournamentFactory(active=True)
        self.deck = DeckFactory()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_tournaments_are_shown_correctly(self):
        self.other_tournament = TournamentFactory(active=True)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, self.tournament.name)
        self.assertContains(response, self.other_tournament.name)
        self.assertContains(response, self.tournament.get_remaining_spots())

    def test_shows_only_active_tournaments(self):
        self.other_tournament = TournamentFactory(active=False)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, self.tournament.name)
        self.assertNotContains(response, self.other_tournament.name)

    def test_decks_are_shown_correctly(self):
        self.other_deck = DeckFactory()
        response = self.client.get(self.url)
        self.assertContains(response, self.deck.name)
        self.assertContains(response, self.other_deck.name)


class TournamentDetailTests(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.tournament = TournamentFactory()
        self.client = Client()
        self.url = reverse_lazy('tournament:tournament-detail', kwargs={'pk': self.tournament.pk})

    def test_can_access_tournament_detail_if_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, self.tournament.name)
        self.assertContains(response, self.tournament.get_remaining_spots())

    def test_can_not_access_tournament_detail_if_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(302, response.status_code)

    def test_can_signup_successfully(self):
        self.player = PlayerFactory(user=self.user)
        self.client.force_login(self.player.user)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(self.player.tournaments.all(), [])
        self.client.post(reverse_lazy('tournament:tournament-signup', kwargs={'pk': self.tournament.pk}))
        self.assertQuerysetEqual(self.player.tournaments.all(), ['<Tournament: {}>'.format(self.tournament)])
        response = self.client.get(self.url)
        self.assertContains(response, "Current number of players: 1")

    def test_can_not_access_signup_if_not_authenticated(self):
        response = self.client.post(reverse_lazy('tournament:tournament-signup', kwargs={'pk': self.tournament.pk}))
        self.assertEqual(302, response.status_code)

    def tearDown(self):
        self.client.logout()
