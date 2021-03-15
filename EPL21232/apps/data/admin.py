from django.contrib import admin
from .models import Station, Data, Mean, Intensity
from .forms import CustomConfirmImportForm, CustomImportForm
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .resources import DataResource

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']


admin.site.register(Station, StationAdmin)

class DataAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DataResource
    list_display = ("tilting_date", "tilting_time", "tilting_number", "tilting_mm")

    def get_import_form(self):
        print(Mean().calculate_mean_per_day) # Test to see if average works
        return CustomImportForm
    
    def get_confirm_import_form(self):
        return CustomConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        if isinstance(form, CustomImportForm):
            if form.is_valid():
                station = form.cleaned_data['station']
                kwargs.update({'station' : station.id})
                #Insert update command of the other tables here ?
                
        return kwargs 

admin.site.register(Data, DataAdmin)

admin.site.register(Mean)
admin.site.register(Intensity)

