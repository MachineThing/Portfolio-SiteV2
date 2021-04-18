from django.core.exceptions import FieldDoesNotExist
from django.core.files.base import ContentFile
from projects.models import GrassGraph
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from pytz import timezone
from PIL import ImageDraw
from io import BytesIO
from PIL import Image
import requests
import json

def index(request):
    # Age handler
    birth_date = datetime(2004, 3, 17)
    today_date = datetime.now(timezone(settings.TIME_ZONE))
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

    bday = (today_date.month, today_date.day) == (birth_date.month, birth_date.day)

    return render(request, 'projects/index.html', {'age':age, 'bday':bday})

def contribCal(request):
    date = datetime.today()
    objects = GrassGraph.manager.get_queryset().filter(year=date.strftime("%y"), week=date.strftime("%U"))
    if len(objects) == 0:
        # Contrib Graph handler
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
        contribCalReq = requests.post('https://api.github.com/graphql', json={'query':ghScript.replace("\n", "")}, headers=head)

        contribCal = json.loads(contribCalReq.text)['data']['user']['contributionsCollection']['contributionCalendar']['weeks']

        # Image handler
        # Image settings
        square_size = 80        # Size of the squares
        square_margin = 32      # Spacing between squares (Multiplied by 2)
        color = (200, 100, 200) # Color of the squares
        maxt = 128              # Maximum transparency
        mint = 48               # Minimum transparency
        zert = 28               # Zero contrib transparency
        maxnum = 0              # Maximum number (Leave at 0)

        for ccx in contribCal:
            for ccy in ccx['contributionDays']:
                if ccy['contributionCount'] > maxnum:
                    maxnum = ccy['contributionCount']
        trat = (maxt-mint)/maxnum

        # Initialize image
        img = Image.new("RGBA", ((square_size+square_margin)*52+square_margin, (square_size+square_margin)*7+square_margin), (0, 0, 0, 136))
        imgd = ImageDraw.Draw(img)

        # Draw rounded squares
        ccx = -1
        ccy = -1
        for squarex in range(square_margin, (square_size+square_margin)*52, square_size+square_margin):
            ccx += 1
            for squarey in range(square_margin, (square_size+square_margin)*7, square_size+square_margin):
                # Get level
                ccy += 1
                level = contribCal[ccx]['contributionDays'][ccy]['contributionCount']
                if ccy >= 6:
                    ccy = -1

                if level == 0:
                    cctn = zert
                else:
                    cctn = round(trat * level)+mint
                imgd.rectangle( # X Rectangle
                    (squarex, squarey+(square_size/4),
                    squarex+square_size, squarey+square_size-(square_size/4)),
                    fill=(color[0], color[1], color[2], cctn)
                )
                imgd.rectangle( # Y Rectangle
                    (squarex+(square_size/4), squarey,
                    squarex+square_size-(square_size/4), squarey+square_size),
                    fill=(color[0], color[1], color[2], cctn)
                )
                imgd.ellipse( # Upper-Left Circle
                    (squarex, squarey,
                    squarex+square_size/2, squarey+square_size/2),
                    fill=(color[0], color[1], color[2], cctn)
                )
                imgd.ellipse( # Upper-Right Circle
                    (squarex+square_size/2, squarey,
                    squarex+square_size, squarey+square_size/2),
                    fill=(color[0], color[1], color[2], cctn)
                )
                imgd.ellipse( # Lower-Left Circle
                    (squarex, squarey+square_size/2,
                    squarex+square_size/2, squarey+square_size),
                    fill=(color[0], color[1], color[2], cctn)
                )
                imgd.ellipse( # Lower-Right Circle
                    (squarex+square_size/2, squarey+square_size/2,
                    squarex+square_size, squarey+square_size),
                    fill=(color[0], color[1], color[2], cctn)
                )
        imgBuff = BytesIO()
        img.save(imgBuff, "PNG")
        grass = GrassGraph.manager.create_grass(ContentFile(imgBuff.getvalue(), 'imgbuff.png'))
    else:
        grass = objects[0]
    return HttpResponse(grass.data, content_type='image/png')
