from django.views.generic.base import RedirectView
from django.core.mail import send_mail
from portfolio.extra.render import render
from django.template.loader import render_to_string
from django.conf import settings
from smtplib import SMTPException
from .captcha import captcha
from .forms import MailForm
from .models import Email

def index(request):
    base_context = {'form':MailForm(), 'recaptcha_public':settings.RECAPTCHA_PUBLIC_KEY}
    if request.method == "POST":
        form = MailForm(request.POST, request.FILES)
        valid_form = form.is_valid()
        try:
            captcha_id = request.POST['captcha_score']
        except KeyError:
            valid_form = False
        if not valid_form:
            base_context['error'] = 'All fields are required.'
            return render(request, 'mailchat/index.html', base_context)
        else:
            try:
                score = captcha(captcha_id)
                verify = form.save(score)
                send_mail(
                    subject = 'Verify your email',
                    message = f'You can verify your email at www.masonfisher.net/mail/verify?v={verify.verify_id}\nIf you received this email in error, you can simply ignore it. Please do not reply to this email!',
                    html_message = render_to_string('mailchat/verify_mail.html', {'verify_url':'www.masonfisher.net/mail?v={}'.format(verify)}),
                    from_email = 'noreply@masonfisher.net',
                    recipient_list = [form.cleaned_data['email']],
                    fail_silently = False)
                base_context['success'] = 'Please check your email for a verification email.'
                return render(request, 'mailchat/index.html', base_context)
            except SMTPException:
                base_context['error'] = 'The email cannot be sent due to an invalid email'
                return render(request, 'mailchat/index.html', base_context)
    else:
        return render(request, 'mailchat/index.html', base_context)

def verify(request):
    verify_id = request.GET.get('v', None)
    if verify_id == None:
        RedirectView.as_view(url='/mail', permanent=False)
    else:
        email = Email.objects.all().filter(verify_url=verify_id)
        if len(email) == 0:
            return render(request, 'mailchat/verified.html', {'type':'danger', 'message':'Your verification has expired.'})
        else:
            email = email[0]
            send_mail(
                subject = f'Email from {email.sendee}',
                message = email.message,
                from_email = 'postoffice@masonfisher.net',
                recipient_list = ['mason@masonfisher.net'],
                fail_silently = False)
            email.delete()
            return render(request, 'mailchat/verified.html', {'type':'success', 'message':'Your email has been sent, please have a good day!'})
