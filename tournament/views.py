from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from rest_framework import generics

from tournament.models import Deck, Bracket, Match, Player, Tournament
from tournament.serializers import (DeckSerializer, BracketSerializer,
                                    MatchSerializer, PlayerSerializer,
                                    TournamentSerializer, UserSerializer)
from tournament.forms import PlayerModelForm

from django.contrib.auth.models import User

from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['active_tournaments'] = Tournament.objects.get_active_tournaments()
        return context


class RegisterFormView(generic.View):
    template_name = 'website/register.html'
    form_class = PlayerModelForm
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PlayerModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            rank = form.cleaned_data.get('rank')
            battle_tag = form.cleaned_data.get('battle_tag')
            user = User.objects.create_user(username=username, password=password)
            player = Player(rank=rank, battle_tag=battle_tag)
            player.user = user
            player.save()
            return redirect(reverse_lazy('tournament:index'))
        else:
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


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
