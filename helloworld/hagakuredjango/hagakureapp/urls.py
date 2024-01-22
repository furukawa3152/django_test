# app/urls.py
from django.urls import path
from .views import index, voice, saga_bot, trans_sagaben, indext5explain

urlpatterns = [
    path('', index, name='index'),
    path('voice/', voice, name='voice'),
    #path('exam/', exam, name='exam'),
    path('saga_bot/', saga_bot, name='saga_bot'),
    path('trans_sagaben/', trans_sagaben, name='trans_sagaben'),
    path('indext5explain/', indext5explain, name='indext5explain'),
]