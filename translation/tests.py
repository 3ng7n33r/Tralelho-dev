from django.test import TestCase

from .models import Country, Language


class IndexTestCase(TestCase):
    def setUp(self):
        Language.objects.create(
            langcode="eng",
            Name_fr="Anglais",
            Name_eng="English",
            Translated="True",
        )
        Language.objects.create(
            langcode="fra",
            Name_fr="Fran\u00e7ais",
            Name_eng="French",
            Translated="True"
        )
        Language.objects.create(
            langcode="deu",
            Name_fr="Allemand",
            Name_eng="German",
            Translated="True"
        )
        Country.objects.create(
            Name_eng="Germany",
            Name_fr="Allemagne",
            countrycode="deu",
            Continent="EU",
            spoken_languages=[
                3
            ]
        )
        Country.objects.create(
            Name_eng="France",
            Name_fr="France",
            countrycode="fra",
            Continent="EU",
            spoken_languages=[
                2
            ]
        )
        Country.objects.create(
            Name_eng="Switzerland",
            Name_fr="Suisse",
            countrycode="che",
            Continent="EU",
            spoken_languages=[
                14,
                24
            ]
        )
        Country.objects.create(
            Name_eng="Madagascar",
            Name_fr="Madagascar",
            countrycode="mdg",
            Continent="AF",
            spoken_languages=[
                1,
                2,
            ]
        )
