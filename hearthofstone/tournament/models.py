from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from tournament.query import TournamentQuerySet


class Deck(models.Model):
    name = models.CharField(max_length=30)
    screenshot = models.ImageField(upload_to='screens', null=True, blank=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    active = models.BooleanField(default=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    max_players = models.IntegerField(default=20)

    def __str__(self):
        return self.name

    def is_active(self):
        return active

    objects = TournamentQuerySet.as_manager()


class Match(models.Model):
    tournament = models.ForeignKey(Tournament)
    active = models.BooleanField(default=True)


class Player(models.Model):
    user = models.OneToOneField(User)
    tournaments = models.ManyToManyField(Tournament, related_name='tournament_players', blank=True)
    rank = models.SmallIntegerField(null=True, blank=True)
    decks = models.ManyToManyField(Deck, related_name='deck_players', blank=True)
    matches = models.ManyToManyField(Match, related_name='match_players', blank=True)
    battle_tag = models.CharField(max_length=256, default='#nameXXXX')

    def __str__(self):
        return self.user.username


class Bracket(models.Model):
    WINNER = 'w'
    LOSER = 'l'
    BRACKET_CHOICES = (
        (WINNER, 'winner'),
        (LOSER, 'loser'),
    )
    name = models.CharField(max_length=256)
    bracket_type = models.CharField(
        max_length=1,
        choices=BRACKET_CHOICES,
        default=WINNER
    )
    tournament = models.ForeignKey(Tournament)

    def __str__(self):
        return self.name
