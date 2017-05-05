from django.conf.urls import url

from tournament import views


apiurlpatterns = [
    url(r'^players/$', views.PlayerList.as_view(), name='player-list-api'),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view(), name='player-detail-api'),
    url(r'^tournaments/$', views.TournamentList.as_view(), name='tournament-list-api'),
    url(r'^tournaments/(?P<pk>[0-9]+)/$', views.TournamentDetail.as_view(), name='tournament-detail-api'),
    url(r'^brackets/$', views.BracketList.as_view(), name='bracket-list-api'),
    url(r'^brackets/(?P<pk>[0-9]+)/$', views.BracketDetail.as_view(), name='bracket-detail-api'),
    url(r'^decks/$', views.DeckList.as_view(), name='deck-list-api'),
    url(r'^decks/(?P<pk>[0-9]+)/$', views.DeckDetail.as_view(), name='deck-detail-api'),
    url(r'^matches/$', views.MatchList.as_view(), name='match-list-api'),
    url(r'^matches/(?P<pk>[0-9]+)/$', views.MatchDetail.as_view(), name='match-detail-api'),
]

regularurlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]

urlpatterns = apiurlpatterns + regularurlpatterns
