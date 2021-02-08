from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:base_language>/<str:base_flag>', views.index, name='index'),
    # ex: /de/
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>',
         views.translation, name='translation'),
    path('support', views.support, name='support'),
    path('<str:base_language>/<str:base_flag>/support',
         views.support, name='support'),
    path('about', views.about, name='about'),
    path('<str:base_language>/<str:base_flag>/about',
         views.about, name='about'),
    path('<str:base_language>/<str:base_flag>/disclaimer',
         views.disclaimer, name='disclaimer'),
    path('<str:base_language>/ajax_calls/search/', views.autocompleteModel),
]

# Docs
urlpatterns += [
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>/documents',
         views.documents, name='documents'),
    path('<str:base_language>/<str:base_flag>/documents',
         views.docindex, name='docindex'),
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>/<str:template>',
         views.doctemplate, name='doctemplate'),
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>/<str:template>/pdf',
         views.generate_pdf, name='generate-pdf'),
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>/<str:template>/pdf/download',
         views.download_pdf, name='download-pdf'),
]
