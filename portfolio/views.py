from django.views.generic.base import RedirectView
from portfolio.extra.grass import grass as gengrass
from datetime import datetime, timedelta
from portfolio.extra.render import render
from projects.models import StaticPage
from django.http import HttpResponse
from django.conf import settings
import pytz

def index(request):
    # Age handler
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(pytz.timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    bday = (today_date.month, today_date.day) == (birth_date.month, birth_date.day)

    return render(request, 'home/index.html', {'age':age, 'bday':bday})

def staticpage(request, pagename):
    try:
        page = StaticPage.objects.filter(html_safe_name__contains=pagename)[0]
    except IndexError:
        # TODO: I should return a 404 page
        raise Exception('TODO: I should return a 404 page')
    html = open(page.html.path)
    htmlfile = html.read()
    html.close()
    if page.template:
        return render(request, 'home/static.html', {'staticpage':htmlfile})
    else:
        return HttpResponse(htmlfile)

def contribCal(request):
    timezone = pytz.timezone(settings.TIME_ZONE)
    date = datetime.now(timezone)

    grass = gengrass(date)
    if date.weekday() == 6:
        expire_date = date + timedelta(days=7)
    else:
        expire_date = date - timedelta(days=date.weekday()-6)
    expire_date = expire_date.replace(hour=0, minute=0, second=0)
    # UTC+0 is the same as GMT
    expire_date = expire_date.astimezone(pytz.utc)

    expire_http_date = expire_date.strftime("Sun, %d %b %Y %H:%M:%S GMT") # Should be Sunday no matter what.

    imgResp = HttpResponse(grass.data, content_type='image/png')
    imgResp['Expires'] = expire_http_date
    return imgResp

# Favicon redirect
favicon = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
