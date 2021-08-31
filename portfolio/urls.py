from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.urls import path
import projects.views
import projects.urls
import mailchat.urls
from . import views as pviews

urlpatterns = [
    path('', pviews.index, name='home'),
    path('favicon.ico', pviews.favicon),
    path('contribCalImg', pviews.contribCal),
    path('admin/', admin.site.urls),
    path('projects/', include(projects.urls)),
    path('staticpage/<str:pagename>', pviews.staticpage, name='home'),
    path('mail/', include(mailchat.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
