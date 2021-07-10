from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
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
                verify = form.save()
                send_mail(
                    subject = 'Verify your email',
                    message = 'You can verify your email at www.masonfisher.net/mail?v={}\nIf you received this email in error, you can simply ignore it. Please do not reply to this email!'.format(verify),
                    html_message = render_to_string('mailchat/verify_mail.html', {'verify_url':'www.masonfisher.net/mail?v={}'.format(verify)}),
                    from_email = 'noreply@masonfisher.net',
                    recipient_list = [form.cleaned_data['email']],
                    fail_silently = False)
                return render(request, 'mailchat/index.html', {'form':MailForm(), 'success':'Your email has been sent!'})
            except SMTPException:
                return render(request, 'mailchat/index.html', {'form':MailForm(), 'error':'The email cannot be sent due to an invalid email'})
    else:
        return render(request, 'mailchat/index.html', {'form':MailForm()})
