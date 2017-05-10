from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tournament.models import Player


class BaseUserPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return True


class NotLoginRequiredMixin(BaseUserPassesTestMixin):

    raise_exception = False

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        return True and super().test_func()


class ProfileObjectMixin(SingleObjectMixin):
    model = Player
    fields = ('rank', 'battle_tag')

    def get_object(self):
        """ Return the current user's profile """
        try:
            return self.request.user.player
        except Player.DoesNotExist:
            raise NotImplemented("No profile, I guess.")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        klass = ProfileObjectMixin
        return super(klass, self).dispatch(request, *args, **kwargs)
