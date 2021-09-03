from django.db import models

class Email(models.Model):
    sendee = models.EmailField()
    sending_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    captcha_score = models.FloatField(null=True)
    verify_url = models.CharField(max_length=15)

    def __str__(self):
        return self.sendee
