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
    context = {
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    return render(request, 'translation/language.html', context)


def documents(request, language_id):
    context = {'language_id': language_id}
    return render(request, 'translation/language.html', context)


def docindex(request):
    return render(request, 'translation/docindex.html')


def support(request):
    return render(request, 'translation/support.html')


def about(request):
    return render(request, 'translation/about.html')
