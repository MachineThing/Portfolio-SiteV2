from django.contrib import admin
from django.urls import path
import projects.views as pviews

urlpatterns = [
    path('', pviews.index, name='projects_home'),
]
