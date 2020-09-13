from django.contrib import admin

# Register your models here.

from .models import Entity
from .models import yearlydata

admin.site.register(Entity)
admin.site.register(yearlydata)
