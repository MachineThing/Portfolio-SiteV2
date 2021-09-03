from django.core.management.base import BaseCommand, CommandError
from mailchat.models import Email
from datetime import timedelta
from datetime import datetime

class Command(BaseCommand):
    help = 'Deletes unverified emails if they are older than a day.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        emails = Email.objects.all()
        emails_deleted = 0

        datelimit = datetime.utcnow() - timedelta(hours=24)
        for email in emails:
            sending_date = email.sending_date.replace(tzinfo=None)
            if sending_date < datelimit:
                email.delete()
                self.stdout.write(f'Deleted email sent by {email.sendee}!')
                emails_deleted += 1

        if emails_deleted != 0:
            self.stdout.write(self.style.SUCCESS(f'Deleted {emails_deleted} unverified emails!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Deleted no unverified emails!'))
