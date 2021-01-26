from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render

from .models import Countries

for country in Countries.objects.all():
    for language in country.spoken_languages.all():
        if not language.Translated:
            language.delete()


AF = Countries.objects.filter(Continent__iexact="AF")
NA = Countries.objects.filter(Continent__iexact="NA")
SA = Countries.objects.filter(Continent__iexact="SA")
OC = Countries.objects.filter(Continent__iexact="OC")
AS = Countries.objects.filter(Continent__iexact="AS")
EU = Countries.objects.filter(Continent__iexact="EU")
continents = {
    'Afrique': AF,
    'Amerique du Nord': NA,
    'Amerique du Sud': SA,
    'Océanie': OC,
    'Asie': AS,
    'Europe': EU,
}


def index(request, base_language="fra", base_flag="fra"):
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/index.html', context)


def translation(request, base_language, base_flag, target_language, target_flag):
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    return render(request, 'translation/language.html', context)


def docindex(request, base_language="fra", base_flag="fra"):
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/docindex.html', context)


def documents(request, base_language, base_flag, target_language, target_flag):
    docs = {
        "Anesthésie": "ane",
        "IRM": "irm",
        "Patient": "pat",
        "Pédiatrie": "ped",
        "Scanner": "scn",
        "Secrétariat": "sec"}
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
        'docs': docs,
    }
    return render(request, 'translation/documents.html', context)


def support(request, base_language="fra", base_flag="fra"):
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/support.html', context)


def about(request, base_language="fra", base_flag="fra"):

    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/about.html', context)
