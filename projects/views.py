from portfolio.extra.render import render

def index(request):
    return render(request, 'projects/index.html', {})
