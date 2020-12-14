from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render

from .models import Countries


def index(request, base_language="fra", base_flag="fra"):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/index.html', context)


def translation(request, base_language, base_flag, target_language, target_flag):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    return render(request, 'translation/language.html', context)


def docindex(request, base_language="fra", base_flag="fra"):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/docindex.html', context)


def documents(request, base_language, base_flag, target_language, target_flag):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    docs = {
        "Anesthésie": "ane",
        "IRM": "irm",
        "Patient": "pat",
        "Pédiatrie": "ped",
        "Scanner": "scn",
        "Secrétariat": "sec"}
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
        'docs': docs,
    }
    return render(request, 'translation/documents.html', context)


def support(request, base_language="fra", base_flag="fra"):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/support.html', context)


def about(request, base_language="fra", base_flag="fra"):
    afrique = Countries.objects.filter(Continent__iexact="Afrique")
    namerique = Countries.objects.filter(Continent__iexact="Amerique du Nord")
    samerique = Countries.objects.filter(Continent__iexact="Amerique du Sud")
    oceanie = Countries.objects.filter(Continent__iexact="Oceania")
    asie = Countries.objects.filter(Continent__iexact="Asie")
    europe = Countries.objects.filter(Continent__iexact="Europe")
    context = {
        'afrique': afrique,
        'namerique': namerique,
        'samerique': samerique,
        'oceanie': oceanie,
        'asie': asie,
        'europe': europe,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/about.html', context)
