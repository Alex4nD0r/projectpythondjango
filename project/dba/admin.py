from django.contrib import admin
from .models import Demand, Geo, Index, Skills

# Register your models here.

admin.site.register(Index)
admin.site.register(Demand)
admin.site.register(Geo)
admin.site.register(Skills)