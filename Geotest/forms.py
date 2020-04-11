from django import forms

class NameInputForm(forms.Form):
    players_name = forms.CharField(label='Dein Name', max_length=100)