from django import forms
from django.utils.html import strip_tags


from .models import Twit


class TwitForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={'placeholder': 'Twit', 'class': 'form-control'}))

    class Meta:
        model = Twit
        exclude = ('user',)
