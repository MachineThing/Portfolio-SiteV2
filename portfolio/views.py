from django.views.generic.base import RedirectView

# Favicon redirect
favicon = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
