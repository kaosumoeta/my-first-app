from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'ababa'
urlpatterns = [
    path('kaoruko/', views.index, name = 'kaoruko')
]