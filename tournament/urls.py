from django.conf.urls import url

from tournament.views import main_views as views
from tournament.views import api_views


apiurlpatterns = [
    url(r'^players/$', api_views.PlayerList.as_view(), name='player-list-api'),
    url(r'^players/(?P<pk>[0-9]+)/$', api_views.PlayerDetail.as_view(), name='player-detail-api'),
    url(r'^tournaments/$', api_views.TournamentList.as_view(), name='tournament-list-api'),
    url(r'^tournaments/(?P<pk>[0-9]+)/$', api_views.TournamentDetail.as_view(), name='tournament-detail-api'),
    url(r'^brackets/$', api_views.BracketList.as_view(), name='bracket-list-api'),
    url(r'^brackets/(?P<pk>[0-9]+)/$', api_views.BracketDetail.as_view(), name='bracket-detail-api'),
    url(r'^decks/$', api_views.DeckList.as_view(), name='deck-list-api'),
    url(r'^decks/(?P<pk>[0-9]+)/$', api_views.DeckDetail.as_view(), name='deck-detail-api'),
    url(r'^matches/$', api_views.MatchList.as_view(), name='match-list-api'),
    url(r'^matches/(?P<pk>[0-9]+)/$', api_views.MatchDetail.as_view(), name='match-detail-api'),
]

regularurlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'tournament/(?P<pk>[0-9]+)/$', views.TournamentDetailView.as_view(), name='tournament-detail'),
    url(r'tournament/(?P<pk>[0-9]+)/sign-up/$', views.TournamentSignUpView.as_view(), name='tournament-signup'),
    url(r'create-deck/$', views.DeckCreateView.as_view(), name='deck-create')
]

urlpatterns = apiurlpatterns + regularurlpatterns
