from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from .forms import CustomConfirmImportForm, CustomImportForm
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .resources import DataResource
from django.dispatch import receiver
from import_export.signals import post_import



class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ("name","longitude","latitude")
    search_fields = ('name',)


# class MeanDayInline(admin.StackedInline):
#    model = MeanDay
#    extra = 1
#    readonly_fields=("mean_per_day",)

           
class DataAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DataResource
    import_template_name = 'admin/import_export/import.html'
    list_display = ("station", "date", "heure", "mesure")
    # readonly_fields=("valuetest",)
    def get_import_form(self):
        # Uncomment only if data is stored already in the database
        # MeanDay().calculate_mean_per_day # Test to see if average works
        # MeanYear().calculate_mean_per_year
        return CustomImportForm
    search_fields = ('station__name', 'date',)
    
#     def get_confirm_import_form(self):
#         return CustomConfirmImportForm

#     def get_form_kwargs(self, form, *args, **kwargs):
#         if isinstance(form, CustomImportForm):
#             if form.is_valid():
#                 station = form.cleaned_data['station']
#                 kwargs.update({'station' : station.id})
#                 #Insert update command of the other tables here ?
                
#         return kwargs 
    
#     inlines = [MeanDayInline]
    
    # inlines = [MeanDayInline]

@receiver(post_import, dispatch_uid='update_means')
def _post_import(model, **kwargs):
    MeanDay().calculate_mean_per_day
    MeanWeek().calculate_mean_per_week
    MeanYear().calculate_mean_per_year
    Intensity().calculate_intensity

class MeanDayAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_day", "mean_per_day", "min_per_day","max_per_day",)
    search_fields = ('station__name', 'mean_day',)


class MeanWeekAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_week", "mean_per_week", "min_per_week","max_per_week",)
    search_fields = ('station__name', 'mean_week',)


class MeanYearAdmin(admin.ModelAdmin):
    list_display = ("station", "mean_year", "mean_per_year", "min_per_year","max_per_year",)
    search_fields = ('station__name', 'mean_year',)

class IntensityAdmin(admin.ModelAdmin):
    list_display = ("station", "intensity_day", "duration", "intensity", "max_amount", "start_interval","end_interval",)
    search_fields = ('station__name', 'intensity_day', 'duration',)


admin.site.register(Station, StationAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(MeanDay,MeanDayAdmin)
admin.site.register(MeanWeek, MeanWeekAdmin)
admin.site.register(MeanYear, MeanYearAdmin)
admin.site.register(Intensity, IntensityAdmin)

