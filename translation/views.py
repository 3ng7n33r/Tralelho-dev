from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render


def index(request):
    return render(request, 'translation/index.html')


def translation(request, language_id):
    context = {'language_id': language_id}
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
