from django.http import HttpResponse
from django.utils.translation import ugettext as _


def index(request):
    message = _("Hello, world. You're at the translation index.")
    return HttpResponse(message)


def translation(request, language_id):
    return HttpResponse("You're translating %s." % language_id)
