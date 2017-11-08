from random import choice

from django.core.management.base import BaseCommand

from tournament.factories import (
    TournamentFactory,
    DeckFactory,
    MatchFactory,
    PlayerFactory,
    BracketFactory
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tournaments = TournamentFactory.create_batch(5)
        decks = DeckFactory.create_batch(5)
        for _ in range(5):
            MatchFactory(tournament=choice(tournaments))

        for _ in range(5):
            PlayerFactory(tournaments=[choice(tournaments)], decks=[choice(decks)])

        for _ in range(5):
            BracketFactory(tournament=choice(tournaments))
