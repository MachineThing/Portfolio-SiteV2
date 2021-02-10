from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone

def index(request):
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    return render(request, 'projects/index.html', {'age': age})
