from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Incubator)
admin.site.register(models.Incubatorusing)
admin.site.register(models.Monitorinform)
admin.site.register(models.Plant)
admin.site.register(models.Alterenvironment)
admin.site.register(models.Buypost)
admin.site.register(models.Sellpost)
admin.site.register(models.Commentpost)
admin.site.register(models.ChangeLog)
admin.site.register(models.ViewParam)