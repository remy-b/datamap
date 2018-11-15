from django.contrib import admin
from .models import Log, Sensor

admin.site.register(Sensor)
admin.site.register(Log)
