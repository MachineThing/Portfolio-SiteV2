from django.contrib import admin
from django.urls import path
import projects.views

urlpatterns = [
    path('', projects.views.index),
    path('admin/', admin.site.urls),
]
