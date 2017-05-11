from rest_framework import generics

from tournament.models import Deck, Bracket, Match, Player, Tournament
from tournament.serializers import (DeckSerializer, BracketSerializer,
                                    MatchSerializer, PlayerSerializer,
                                    TournamentSerializer, UserSerializer)
from django.contrib.auth.models import User


# API views
class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class BracketList(generics.ListCreateAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


class BracketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
