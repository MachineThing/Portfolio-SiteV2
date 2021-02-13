from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone
from PIL import ImageDraw
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
    square_size = 30
    square_margin = 12 # Multiplied by 2
    weeks = 52
    color = (0, 200, 0)
    maxt = 128

    img = Image.new("RGBA", ((square_size+square_margin)*weeks+square_margin, (square_size+square_margin)*7+square_margin), (0, 0, 0, 136))
    imgd = ImageDraw.Draw(img)

    # Draw rounded squares
    for squarex in range(square_margin, (square_size+square_margin)*weeks, square_size+square_margin):
        for squarey in range(square_margin, (square_size+square_margin)*7, square_size+square_margin):
            imgd.rectangle( # X Rectangle
                (squarex, squarey+(square_size/4),
                squarex+square_size, squarey+square_size-(square_size/4)),
                fill=(color[0], color[1], color[2], maxt)
            )
            imgd.rectangle( # Y Rectangle
                (squarex+(square_size/4), squarey,
                squarex+square_size-(square_size/4), squarey+square_size),
                fill=(color[0], color[1], color[2], maxt)
            )
            imgd.ellipse( # Upper-Left Circle
                (squarex, squarey,
                squarex+square_size/2, squarey+square_size/2),
                fill=(color[0], color[1], color[2], maxt)
            )
            imgd.ellipse( # Upper-Right Circle
                (squarex+square_size/2, squarey,
                squarex+square_size, squarey+square_size/2),
                fill=(color[0], color[1], color[2], maxt)
            )
            imgd.ellipse( # Lower-Left Circle
                (squarex, squarey+square_size/2,
                squarex+square_size/2, squarey+square_size),
                fill=(color[0], color[1], color[2], maxt)
            )
            imgd.ellipse( # Lower-Right Circle
                (squarex+square_size/2, squarey+square_size/2,
                squarex+square_size, squarey+square_size),
                fill=(color[0], color[1], color[2], maxt)
            )
    imgBuff = BytesIO()
    img.save(imgBuff, "PNG")
    return HttpResponse(imgBuff.getvalue(), content_type='image/png')
