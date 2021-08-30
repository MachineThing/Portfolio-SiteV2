from django.core.management.base import BaseCommand, CommandError
from projects.models import GrassGraph
from datetime import datetime

class Command(BaseCommand):
    help = 'Deletes grass graphs older than 3 weeks.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        grasses = GrassGraph.manager.all()
        grasses_deleted = 0
        for grass in grasses:
            grass_week = int(grass.week)
            date = datetime.today()
            week = int(date.strftime("%U"))
            if week < grass_week:
                grass_week -= 52 # A year is 52 weeks (minus leap years)
            if grass_week < week-3:
                grass.data.delete() # Delete image
                grass.delete() # Delete entire model object
                grasses_deleted += 1
                self.stdout.write(f'Week {grass_week} deleted!')
        if grasses_deleted != 0:
            self.stdout.write(self.style.SUCCESS(f'Deleted {grasses_deleted} grass graphs!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Deleted no grass graphs!'))
