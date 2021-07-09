from django.core.mail import send_mail
from django.shortcuts import render
from smtplib import SMTPException
from .forms import MailForm

def index(request):
    if request.POST:
        form = MailForm(request.POST, request.FILES)
        if not form.is_valid():
            print(form.errors)
            return render(request, 'mailchat/index.html', {'form':MailForm(), 'error':'The email cannot be sent due to an invalid form'})
        else:
            try:
                form.save()
                #send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], 'test@example.com', [form.cleaned_data['email']])
                return render(request, 'mailchat/index.html', {'form':MailForm(), 'success':'Your email has been sent!'})
            except SMTPException:
                return render(request, 'mailchat/index.html', {'form':MailForm(), 'error':'The email cannot be sent due to an invalid email'})
    else:
        return render(request, 'mailchat/index.html', {'form':MailForm()})
