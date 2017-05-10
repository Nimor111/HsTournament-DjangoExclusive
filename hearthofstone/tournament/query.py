from django.db import models


class TournamentQuerySet(models.QuerySet):

    def get_active_tournaments(self):
        return self.filter(active=True)[:2]
