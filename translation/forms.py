from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from translation.models import Country


class searchcountryform(forms.Form):
    error_class = 'error'
    countrystring = _("Rechercher un pays")
    country_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(
<<<<<<< HEAD
        attrs={'placeholder': countrystring, 'id': 'txtSearch'}))
=======
        attrs={'placeholder': countrystring, 'id': 'txtSearch', 'name': 'txtSearch'}))
>>>>>>> ed2612bdf30efc9de4cab7df6e481e366faf87d8

    def clean_country_name(self):
        data = self.cleaned_data['country_name']

        try:
            Country.objects.get(Name_eng__iexact=data)
        except:
            raise ValidationError(
                _("Nous n'avons pas trouvé ce pays. Merci de verifier l'orthographe."))
        return data
