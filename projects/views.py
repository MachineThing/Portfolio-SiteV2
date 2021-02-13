from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone
from io import BytesIO
from PIL import Image
import requests

def index(request):
    # Age handler
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    return render(request, 'projects/index.html', {'age': age})

def contribCal(request):
    # Contrib Graph handler
    # TODO: Minimize api requests by storing this into database
    # TODO: Make an image out of this data
    ghScript = """
    {
    user(login:\"MachineThing\") {
        contributionsCollection {
            contributionCalendar {
                weeks {
                    contributionDays {
                        contributionCount
                    }
                }
            }
        }
    }}
    """
    head = {'Content-Type': 'application/json', 'Authorization':'token '+settings.GITHUB_KEY}
    contribCal = requests.post('https://api.github.com/graphql', json={'query':ghScript.replace("\n", "")}, headers=head)

    # Image settings
    square_size = 25
    square_margin = 12
    weeks = 52

    img = Image.new("RGBA", ((square_size+square_margin)*weeks, (square_size+square_margin)*7), (255, 0, 0, 136))
    imgBuff = BytesIO()
    img.save(imgBuff, "PNG")
    return HttpResponse(imgBuff.getvalue(), content_type='image/png')
