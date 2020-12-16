from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /de/
    path('<str:language_id>/', views.translation, name='translation'),
    path('documents', views.documents, name='documents'),
    path('support', views.support, name='support'),
    path('about', views.about, name='about'),
]
