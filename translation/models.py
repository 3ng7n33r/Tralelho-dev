from django.db import models


class Language(models.Model):
    """ Iso-639-2/T """
    langcode = models.CharField(max_length=3, unique=True)
    Name_fr = models.CharField(max_length=50, unique=True)
    Name_eng = models.CharField(max_length=50, unique=True)
    Translated = models.BooleanField(default=False)

    def __str__(self):
        return self.Name_fr

    class Meta:
        ordering = ['Name_fr']


class Country(models.Model):
    """ ISO 3166 - 1 - alpha3"""
    Continent_Choices = [
        ('AF', 'Afrique'),
        ('NA', 'Amerique du Nord'),
        ('SA', 'Amerique du Sud'),
        ('OC', 'Océanie'),
        ('AS', 'Asie'),
        ('EU', 'Europe'),
    ]

    countrycode = models.CharField(max_length=3, unique=True)
    Name_fr = models.CharField(max_length=50, unique=True)
    Name_eng = models.CharField(max_length=50, unique=True)
    spoken_languages = models.ManyToManyField(Language)
    Continent = models.CharField(max_length=50, choices=Continent_Choices)
    Continent2 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Name_fr

    class Meta:
        ordering = ['Name_fr']

    def translated_spoken_languages(self, base_language="None"):
        return self.spoken_languages.filter(Translated=True).exclude(langcode=base_language)


# resources:
# http://www.i18nguy.com/unicode/language-identifiers.html
# http://download.geonames.org/export/dump/countryInfo.txt
