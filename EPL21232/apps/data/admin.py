from django.contrib import admin
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from .forms import CustomConfirmImportForm, CustomImportForm
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .resources import DataResource

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']


admin.site.register(Station, StationAdmin)

class MeanDayInline(admin.StackedInline):
    model = MeanDay
    extra = 1
    readonly_fields=("mean_per_day",)

           
class DataAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DataResource
    list_display = ("station", "tilting_date", "tilting_time", "tilting_number", "tilting_mm","valuetest","name")
    readonly_fields=("valuetest",)

    def get_import_form(self):
        # Uncomment only if data is stored already in the database
        print(MeanDay().calculate_mean_per_day) # Test to see if average works
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
    
    inlines = [MeanDayInline]
    #print(MeanDay().mean_day_real)


class MeanDayAdmin(admin.ModelAdmin):
    list_display = ("mean_day_real", "mean_per_day_real")

           

admin.site.register(Data, DataAdmin)
admin.site.register(MeanDay,MeanDayAdmin)
admin.site.register(MeanWeek)
admin.site.register(MeanYear)
admin.site.register(Intensity)

