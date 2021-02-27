from django.contrib import admin
from .models import Station, Data

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']


admin.site.register(Station, StationAdmin)

admin.site.register(Data)

