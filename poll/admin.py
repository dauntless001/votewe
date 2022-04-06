from django.contrib import admin
from poll import models
# Register your models here.


admin.site.register(models.Agent)
admin.site.register(models.LGA)
admin.site.register(models.PollingUnit)
admin.site.register(models.Party)
admin.site.register(models.State)
admin.site.register(models.Ward)
admin.site.register(models.Result)