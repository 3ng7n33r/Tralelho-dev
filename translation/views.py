from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .models import Country
from translation.forms import searchcountryform

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
import json


# sort countries by continent
AF = Country.objects.order_by('Name_eng').filter(Continent__iexact="AF")
NA = Country.objects.order_by('Name_eng').filter(Continent__iexact="NA")
SA = Country.objects.order_by('Name_eng').filter(Continent__iexact="SA")
OC = Country.objects.order_by('Name_eng').filter(Continent__iexact="OC")
AS = Country.objects.order_by('Name_eng').filter(Continent__iexact="AS")
EU = Country.objects.order_by('Name_eng').filter(Continent__iexact="EU")
continents = {
    _('Afrique'): AF,
    _('Amerique du Nord'): NA,
    _('Amerique du Sud'): SA,
    _('Océanie'): OC,
    _('Asie'): AS,
    _('Europe'): EU,
}


def autocompleteModel(request, base_language):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Country.objects.filter(Name_eng__startswith=q).filter(
            spoken_languages__Translated=True).exclude(spoken_languages__langcode=base_language)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.Name_eng)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


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
            elif len(language) > 1:
                return HttpResponseRedirect("".join(('/', base_language, '/', base_flag, '#', countryform.countrycode, 'target', )))
            else:
                raise ValidationError(
                    _("Nous n'avons pas trouvé ce pays. Merci de verifier l'orthographe"))

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
        _("IRM"): "irm",
        _("Scanner"): "scn",
    }
    context = {
        'continents': continents,
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
        'docs': docs,
    }
    return render(request, 'translation/documents.html', context)


'''     docs = {
        "Anesthésie": "ane",
        "IRM": "irm",
        "Patient": "pat",
        "Pédiatrie": "ped",
        "Scanner": "scn",
        "Secrétariat": "sec"
        } '''


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


def generate_pdf(request, base_language, base_flag, target_language, target_flag, template):
    context = {
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={x}-{y}-IRM.pdf".format(
        x=base_language,
        y=target_language,
    )
    html = render_to_string(
        'doctemplates/{template}.html'.format(template=template), context)

    font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response, font_config=font_config)
    return response


def download_pdf(request, base_language, base_flag, target_language, target_flag, template):
    context = {
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "attachment; filename={x}-{y}-IRM.pdf".format(
        x=base_language,
        y=target_language,
    )
    html = render_to_string(
        'doctemplates/{template}.html'.format(template=template), context)

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response


def doctemplate(request, base_language, base_flag, target_language, target_flag, template):

    context = {
        'base_language': base_language,
        'base_flag': base_flag,
        'target_language': target_language,
        'target_flag': target_flag,
    }
    return render(request, 'doctemplates/{template}.html'.format(template=template), context)
