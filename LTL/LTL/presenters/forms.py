from django import forms

from LTL.presenters import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ('user', )