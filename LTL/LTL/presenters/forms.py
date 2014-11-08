from django import forms

from LTL.presenters import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ('user', )


class TalkForm(forms.ModelForm):
    when = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = models.Talk
        exclude = ('presenter', )
