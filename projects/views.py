from portfolio.gen.grass import grass as gengrass
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import pytz

def index(request):
    # Age handler
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(pytz.timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    bday = (today_date.month, today_date.day) == (birth_date.month, birth_date.day)

    return render(request, 'projects/index.html', {'age':age, 'bday':bday})

def contribCal(request):
    timezone = pytz.timezone(settings.TIME_ZONE)
    date = datetime.now(timezone)
    # UTC+0 is the same as GMT
    GMT_date = date.astimezone(pytz.utc)

    grass = gengrass(date)
    if date.weekday() == 6:
        expire_date = date + timedelta(days=7)
    else:
        expire_date = date - timedelta(days=date.weekday()-6)
    expire_date = expire_date.replace(hour=0, minute=0, second=0)
    expire_date = expire_date.astimezone(pytz.utc)

    http_date = GMT_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
    expire_http_date = expire_date.strftime("Sun, %d %b %Y %H:%M:%S GMT") # Should be Sunday no matter what.

    imgResp = HttpResponse(grass.data, content_type='image/png')
    imgResp['Date'] = http_date # Just incase Django doesn't supply the date in the header in the future for some reason, probably won't but better safe than sorry
    imgResp['Expires'] = expire_http_date
    return imgResp
