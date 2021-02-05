from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.shortcuts import render

from .models import Country
from translation.forms import searchcountryform

# sort countries by continent
AF = Country.objects.order_by('Name_eng').filter(Continent__iexact="AF")
NA = Country.objects.order_by('Name_eng').filter(Continent__iexact="NA")
SA = Country.objects.order_by('Name_eng').filter(Continent__iexact="SA")
OC = Country.objects.order_by('Name_eng').filter(Continent__iexact="OC")
AS = Country.objects.order_by('Name_eng').filter(Continent__iexact="AS")
EU = Country.objects.order_by('Name_eng').filter(Continent__iexact="EU")
continents = {
    'Afrique': AF,
    'Amerique du Nord': NA,
    'Amerique du Sud': SA,
    'Océanie': OC,
    'Asie': AS,
    'Europe': EU,
}


def index(request, base_language="fra", base_flag="fra"):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = searchcountryform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Name_form = form.cleaned_data['country_name']
            countryform = Country.objects.get(Name_eng__iexact=Name_form)

            language = countryform.spoken_languages.filter(
                Translated=True).exclude(langcode=base_language)
            if len(language) == 1:
                return HttpResponseRedirect("".join(('/', base_language, '/', base_flag, '/', language.first().langcode, '/', countryform.countrycode)))
            else:
                return HttpResponseRedirect("".join(('/', base_language, '/', base_flag, '#', countryform.countrycode, 'target', )))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = searchcountryform()

    context = {
        'form': form,
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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = searchcountryform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Name_form = form.cleaned_data['country_name']
            countryform = Country.objects.get(Name_eng__iexact=Name_form)

            language = countryform.spoken_languages.filter(
                Translated=True).exclude(langcode=base_language)
            if len(language) == 1:
                return HttpResponseRedirect("".join(('/', base_language, '/', base_flag, '/', language.first().langcode, '/', countryform.countrycode, '/', 'documents')))
            else:
                return HttpResponseRedirect("".join(('/', base_language, '/', base_flag, '/', 'documents', '#', countryform.countrycode, 'target', )))
        # if a GET (or any other method) we'll create a blank form
    else:
        form = searchcountryform()
    context = {
        'form': form,
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


def disclaimer(request, base_language="fra", base_flag="fra"):

    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
    }
    return render(request, 'translation/disclaimer.html', context)
