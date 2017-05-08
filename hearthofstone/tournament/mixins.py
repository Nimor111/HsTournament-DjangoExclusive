from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class BaseUserPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return True


class NotLoginRequiredMixin(BaseUserPassesTestMixin):

    raise_exception = False

    def test_func(self):
        if self.request.user.is_authenticated:
            return False

        return True and super().test_func()
