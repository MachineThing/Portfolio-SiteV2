from datetime import datetime
from django.db import models

class GGManager(models.Manager):
    def get_grass(self, year=None, week=None):
        date = datetime.today()
        if year == None:
            year = date.strftime("%y")
        if week == None:
            week = date.strftime("%U")
        pass

    def create_grass(self, data):
        date = datetime.today()
        grassGraph = self.create(data=data, year=date.strftime("%y"), week=date.strftime("%U"))
        return grassGraph

class GrassGraph(models.Model):
    data = models.ImageField(upload_to='grass/')
    year = models.CharField(max_length=2)
    week = models.CharField(max_length=2)
    manager = GGManager()

    def __str__(self):
        return "Grass Graph - "+self.year+"_"+self.week
