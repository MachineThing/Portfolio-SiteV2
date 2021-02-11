from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone
import requests

def index(request):
    # Age handler
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

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

    return render(request, 'projects/index.html', {'age': age})
