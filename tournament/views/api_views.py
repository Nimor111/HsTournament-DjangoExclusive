from rest_framework import generics

from tournament.models import Deck, Bracket, Match, Player, Tournament
from tournament.serializers import (DeckSerializer, BracketSerializer,
                                    MatchSerializer, PlayerSerializer,
                                    TournamentSerializer, UserSerializer)
from django.contrib.auth.models import User

from tournament.mixins import IsSuperUserMixin


# API views
class DeckList(IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckDetail(IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class MatchList(IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetail(IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class BracketList(IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


class BracketDetail(IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


class PlayerList(IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlayerDetail(IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TournamentList(IsSuperUserMixin, generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(IsSuperUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
