from django.shortcuts import render

def index(request):
    # TODO: make age dynamic
    return render(request, 'projects/index.html', {'age': 16})
