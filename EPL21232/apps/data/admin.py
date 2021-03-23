from django.contrib import admin
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from .forms import CustomConfirmImportForm, CustomImportForm
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .resources import DataResource
from django.dispatch import receiver
from import_export.signals import post_import

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ("name","longitude","latitude")


# class MeanDayInline(admin.StackedInline):
#    model = MeanDay
#    extra = 1
#    readonly_fields=("mean_per_day",)

           
class DataAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DataResource
    list_display = ("station", "tilting_date", "tilting_time", "tilting_number", "tilting_mm")
    # readonly_fields=("valuetest",)

    def get_import_form(self):
        # Uncomment only if data is stored already in the database
        # MeanDay().calculate_mean_per_day # Test to see if average works
        # MeanYear().calculate_mean_per_year
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
    
    # inlines = [MeanDayInline]

@receiver(post_import, dispatch_uid='update_means')
def _post_import(model, **kwargs):
    MeanDay().calculate_mean_per_day
    MeanWeek().calculate_mean_per_week
    MeanYear().calculate_mean_per_year

class MeanDayAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_day", "min_per_day","max_per_day", "mean_per_day")


class MeanWeekAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_week", "min_per_week","max_per_week", "mean_per_week")


class MeanYearAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_year", "min_per_year","max_per_year", "mean_per_year")

           
admin.site.register(Station, StationAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(MeanDay,MeanDayAdmin)
admin.site.register(MeanWeek, MeanWeekAdmin)
admin.site.register(MeanYear, MeanYearAdmin)
admin.site.register(Intensity)

