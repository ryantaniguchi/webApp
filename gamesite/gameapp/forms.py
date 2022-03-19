from django import forms
from .models import Game

# Form used to add new games to the database
class CreateNewGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('__all__')