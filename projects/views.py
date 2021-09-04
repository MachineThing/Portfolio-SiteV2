from portfolio.extra.render import render
from projects import models

def index(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/index.html', {'projects':projects})
