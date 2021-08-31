from datetime import datetime
from django.db import models

class GGManager(models.Manager):
    def create_grass(self, data):
        date = datetime.today()
        grassGraph = self.create(data=data, year=date.strftime("%y"), week=date.strftime("%U"))
        return grassGraph

class GrassGraph(models.Model):
    data = models.ImageField(upload_to='grass/')
    year = models.CharField(max_length=2)
    week = models.CharField(max_length=2)
    id = models.BigAutoField(primary_key=True)
    manager = GGManager()

    def __str__(self):
        return f"Grass Graph - {self.year}_{self.week}"

class NavBar(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"Navbar - {self.name}"

class StaticPage(models.Model):
    name = models.CharField(max_length=25)
    html_safe_name = models.CharField(max_length=25)
    html = models.FileField(upload_to='html/')
    hidden = models.BooleanField(default=False)
    template = models.BooleanField(default=True)

    navbar = models.ForeignKey("NavBar", default=1, verbose_name="NavBar", on_delete=models.SET_DEFAULT, blank=True, null=True)

    def __str__(self):
        return f"Static Page - {self.name}"

    def delete(self):
        html.delete()
        super(Product, self).delete()
