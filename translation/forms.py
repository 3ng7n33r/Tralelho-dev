from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from translation.models import Country


class searchcountryform(forms.Form):
    error_class = 'error'
    countrystring = _("Search for Country")
    country_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'placeholder': countrystring, 'class': 'form-control', 'id': 'txtSearch', 'name': 'txtSearch'}))

    def clean_country_name(self):
        data = self.cleaned_data['country_name']

        try:
            Country.objects.get(Name_eng__iexact=data)
        except:
            raise ValidationError(
                _('Country not found. Please check spelling'))
        return data
