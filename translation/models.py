from django.db import models


class Countries(models.Model):
    """ Iso-639-2/T """
    langcode = models.CharField(max_length=3)
    """ ISO 3166-1 alpha-3 """
    flagcode = models.CharField(max_length=3)
    Name_fr = models.CharField(max_length=50, unique=True)
    Name_eng = models.CharField(max_length=50, unique=True)
    Continent = models.CharField(max_length=50)
    Continent2 = models.CharField(max_length=50, blank=True)
    Translated = models.BooleanField(default=False)

    def __str__(self):
        return self.Name_eng
