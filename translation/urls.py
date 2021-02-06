from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:base_language>/<str:base_flag>', views.index, name='index'),
    # ex: /de/
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>',
         views.translation, name='translation'),
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>/documents',
         views.documents, name='documents'),
    path('<str:base_language>/<str:base_flag>/documents',
         views.docindex, name='docindex'),
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
