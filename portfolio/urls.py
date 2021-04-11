from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.urls import path
import projects.views
import projects.urls
from . import views as pviews

urlpatterns = [
    path('', projects.views.index),
    path('favicon.ico', pviews.favicon),
    path('contribCalImg', projects.views.contribCal),
    path('admin/', admin.site.urls),
    path('projects/', include(projects.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
