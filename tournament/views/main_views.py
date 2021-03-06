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

from tournament.mixins import ProfileObjectMixin
from tournament.forms import DeckModelForm

# TODO figure this out
# from tournament.mixins import NotLoginRequiredMixin


class IndexView(generic.TemplateView):
    """ Where most of the action happens """
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['active_tournaments'] = Tournament.objects.get_active_tournaments()
        context['random_decks'] = Deck.objects.all()[:3]
        return context


class RegisterFormView(generic.View):
    """ Displays form for user registration and saves it to db"""
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


class ProfileUpdateView(LoginRequiredMixin, ProfileObjectMixin, generic.UpdateView):
    """Form for editing a user's profile"""
    template_name = 'website/user_profile.html'

    def get_success_url(self):
        return reverse_lazy("tournament:index")


class TournamentDetailView(LoginRequiredMixin, generic.DetailView):
    """ View details for a specific tournament, description included"""
    model = Tournament
    template_name = 'website/tournament_detail.html'
    login_url = reverse_lazy('login')
    context_object_name = 'tournament'

    def get_object(self):
        return get_object_or_404(Tournament, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_players_count'] = self.model.objects.get(pk=self.kwargs['pk']).tournament_players.count()
        return context


class TournamentSignUpView(LoginRequiredMixin, generic.View):
    """ Use the sign up button to join an existing tournament"""
    model = Tournament
    template_name = 'website/tournament_detail.html'

    def get_success_url(self):
        return reverse_lazy('tournament:tournament-detail', kwargs={'pk': self.kwargs.get('pk')})

    def post(self, *args, **kwargs):
        tournament = self.model.objects.get(pk=kwargs.get('pk'))
        self.request.user.player.tournaments.add(tournament)
        self.request.user.player.save()
        self.request.user.save()

        return redirect(self.get_success_url())


class DeckCreateView(LoginRequiredMixin, generic.CreateView):
    model = Deck
    template_name = 'website/deck_create.html'
    form_class = DeckModelForm

    def form_valid(self, form):
        form.instance.save()
        self.request.user.player.decks.add(form.instance)
        return super(DeckCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tournament:index')


class Error404(generic.TemplateView):
    """ If any error 404 occurs"""
    template_name = 'website/error404/html'
