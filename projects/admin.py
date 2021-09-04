from django.contrib import admin
# Models
from projects import models

admin.site.register(models.GrassGraph)
admin.site.register(models.NavBar)
admin.site.register(models.StaticPage)
admin.site.register(models.ProjectTag)
admin.site.register(models.Project)
