from django.contrib import admin

# Register your models here.

from .models import Country, Language

admin.AdminSite.site_header = "Tralelho administration page"


def make_translated(modeladmin, request, queryset):
    queryset.update(Translated=True)


make_translated.short_description = "Mark language as translated"


def make_untranslated(modeladmin, request, queryset):
    queryset.update(Translated=False)


make_untranslated.short_description = "Mark language as not translated"


class LanguageAdmin(admin.ModelAdmin):
    fields = ['Name_eng', 'Translated', 'Name_fr', 'langcode']
    list_display = ('Name_eng', 'Translated')
    list_filter = ['Translated']
    search_fields = ['Name_eng', 'Name_fr']
    actions = [make_translated, make_untranslated]


admin.site.register(Language, LanguageAdmin)


class CountryAdmin(admin.ModelAdmin):
    fields = ['Name_eng', 'Name_fr', 'countrycode',
              'spoken_languages', 'Continent', 'Continent2']
    list_display = ('Name_eng', 'Continent', 'translated_languages')
    list_filter = ['Continent']
    search_fields = ['Name_eng', 'Name_fr']

    def translated_languages(self, obj):
        return list(obj.translated_spoken_languages())


admin.site.register(Country, CountryAdmin)
