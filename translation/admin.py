from django.contrib import admin

# Register your models here.

from .models import Countries, Language

admin.site.register(Language)
admin.site.register(Countries)
