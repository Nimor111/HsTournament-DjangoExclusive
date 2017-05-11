import factory
from faker import Factory

from tournament.models import Deck, Tournament, Match, Player, Bracket

from django.contrib.auth.models import User
from datetime import datetime

faker = Factory.create()


class DeckFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Deck

    name = factory.LazyAttribute(lambda _: faker.word())


class TournamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament

    name = factory.LazyAttribute(lambda _: faker.word())
    active = factory.LazyAttribute(lambda _: faker.boolean())
    start_time = factory.LazyAttribute(lambda _: datetime.now())
    end_time = factory.LazyAttribute(lambda _: datetime.now())
    max_players = factory.LazyAttribute(lambda _: faker.pyint())


class MatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Match

    tournament = factory.SubFactory(TournamentFactory)
    active = factory.LazyAttribute(lambda _: faker.boolean())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.word())
    password = 'apassword'
    email = factory.LazyAttribute(lambda _: faker.email())


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Player

    user = factory.SubFactory(UserFactory)
    rank = factory.LazyAttribute(lambda _: faker.pyint())
    battle_tag = factory.LazyAttribute(lambda _: faker.word())

    # call with PlayerFactory(tournaments=(t1, t2, t3))
    @factory.post_generation
    def tournaments(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tournament in extracted:
                self.tournaments.add(tournament)

    @factory.post_generation
    def decks(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for deck in extracted:
                self.decks.add(deck)

    @factory.post_generation
    def matches(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for match in extracted:
                self.matches.add(match)


class BracketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bracket

    name = factory.LazyAttribute(lambda _: faker.word())
    bracket_type = 'w'
    tournament = factory.SubFactory(TournamentFactory)
