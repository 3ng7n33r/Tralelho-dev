from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /de/
    path('<str:language_id>/', views.translation, name='translation'),
]
