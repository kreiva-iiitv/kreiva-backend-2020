from django import forms
from teams.models import *


class TeamForm(forms.ModelForm):

    class Meta:

        model = Team
        fields = '__all__'
