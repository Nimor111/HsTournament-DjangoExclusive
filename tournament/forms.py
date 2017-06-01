from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator

from tournament.models import Player


class PlayerModelForm(UserCreationForm):
    rank = forms.IntegerField(
        required=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(25)
        ])
    battle_tag = forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'rank', 'battle_tag')

    def save(self, commit=True):
        user = super(PlayerModelForm, self).save(commit=False)
        # import ipdb; ipdb.set_trace()
        if commit:
            user.save()
            player = Player.objects.create(user=user, rank=self.cleaned_data['rank'], battle_tag=self.cleaned_data['battle_tag'])
        return user
