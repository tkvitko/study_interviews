from django.contrib import admin
from django.urls import path, include
from .views import list_view, create_good

urlpatterns = [
    path('', list_view, name='goods'),
    path('create', create_good, name='create_good')
]
