from django.contrib import admin
from django.urls import include
from django.urls import path
import projects.views
import projects.urls

urlpatterns = [
    path('', projects.views.index),
    path('contribCalImg', projects.views.contribCal),
    path('admin/', admin.site.urls),
    path('projects/', include(projects.urls))
]
