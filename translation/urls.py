from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:base_language>/<str:base_flag>/', views.index, name='index'),
    # ex: /de/
    path('<str:base_language>/<str:base_flag>/<str:target_language>/<str:target_flag>',
         views.translation, name='translation'),
    path('documents', views.documents, name='documents'),
    path('docindex', views.docindex, name='docindex'),
    path('support', views.support, name='support'),
    path('about', views.about, name='about'),
]
