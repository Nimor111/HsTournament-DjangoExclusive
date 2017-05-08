from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from rest_framework import generics

from tournament.models import Deck, Bracket, Match, Player, Tournament
from tournament.serializers import (DeckSerializer, BracketSerializer,
                                    MatchSerializer, PlayerSerializer,
                                    TournamentSerializer, UserSerializer)
from tournament.forms import PlayerModelForm

from django.contrib.auth.models import User

from django.views import generic
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin

# TODO figure this out
# from tournament.mixins import NotLoginRequiredMixin


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['active_tournaments'] = Tournament.objects.get_active_tournaments()
        context['random_decks'] = Deck.objects.all()[:3]
        return context


class RegisterFormView(generic.View):
    template_name = 'website/register.html'
    form_class = PlayerModelForm
    success_url = '/'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('tournament:index')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PlayerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('tournament:index'))
        else:
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class TournamentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tournament
    template_name = 'website/tournament_detail.html'
    login_url = reverse_lazy('login')
    context_object_name = 'tournament'

    def get_object(self):
        return get_object_or_404(Tournament, pk=self.kwargs['pk'])
