from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from tournament.models import Player


class PlayerModelForm(UserCreationForm):
    rank = forms.IntegerField(required=False)
    battle_tag = forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'rank', 'battle_tag')

    # def save(self, commit=True):
    #     # import ipdb; ipdb.set_trace()
    #     user = super(UserCreationForm, self).save(commit=False)
    #     if commit():
    #         user.save()
    #     player = Player(rank=self.cleaned_data['rank'], battle_tag=self.cleaned_data['battle_tag'])
    #     player.user = user
    #     player.save()
    #     return user
