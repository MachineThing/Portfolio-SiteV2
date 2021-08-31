from django.shortcuts import render as oldrender
from projects import models

def render(request, template_name, context={}, content_type="text/html", status=200, using=None):
    context['navbars'] = models.NavBar.objects.all()
    context['staticpages'] = models.StaticPage.objects.all()
    rendered = oldrender(request, template_name, context, content_type, status, using)
    return rendered
