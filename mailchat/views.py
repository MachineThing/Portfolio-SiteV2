from django.shortcuts import render
from .forms import MailForm

def index(request):
    if request.POST:
        pass
    else:
        return render(request, 'mailchat/index.html', {'form':MailForm()})
