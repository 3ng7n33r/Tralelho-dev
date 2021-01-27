from django.contrib import admin

# Register your models here.

from .models import Country, Language

admin.site.register(Language)
admin.site.register(Country)
