from django import forms
from django.forms import fields

from recommendations.models import Search

class SearchForm(forms.Form):

    class Meta:
        model = Search
        fields = "__all__"