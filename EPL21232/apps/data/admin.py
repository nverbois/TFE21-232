from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from .forms import CustomConfirmImportForm, CustomImportForm
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .resources import DataResource

# class StationAdmin(admin.ModelAdmin):
#     # a list of displayed columns name.
#     list_display = ['name']


# admin.site.register(Station, StationAdmin)

# class DataForm(forms.ModelForm):
#      model = Data

# class MeanDayForm(forms.ModelForm):
#      model = MeanDay

# class MeanDayInlineFormSet(BaseInlineFormSet):
#     def clean(self):
#         super(MeanDayInLineFormSet, self).clean()
#         self.cleaned_data[0]['mean_per_day'] = 5000

#     # def save_new_objects(self, commit=True):
#     #     saved_instances = super(MeanDayInlineFormSet, self).save_new_objects(commit)
#     #     if commit:
#     #         # create book for press
#     #     return saved_instances

#     # def save_existing_objects(self, commit=True):
#     #     saved_instances = super(BookInlineFormSet, self).save_existing_objects(commit)
#     #     if commit:
#     #         # update book for press
#     #   return saved_instances

# class MeanDayInline(admin.TabularInline):
#     model = MeanDay
#     form = MeanDayForm
#     fromset = MeanDayInlineFormSet
#     extra = 1
#     readonly_fields=('mean_per_day','mean_day')

#     # def __init__(self):
#     #     newMeanDay = MeanDay(station = Data.objects.last().station,
#     #                         mean_day =Data.objects.last().tilting_date,
#     #                         mean_per_day = mean_per_day_realone)
        
#     #     newMeanDay.save()
   
#     # def mean_per_day_realone(self):
#     #     var1 = Data.objects
#     #     oldest_date = var1.last().tilting_date
#     #     station = var1.last().station
#     #     mpd = json.dumps(Data.objects.filter(tilting_date=oldest_date).aggregate(Avg('tilting_mm'))['tilting_mm__avg'], use_decimal=True)
#     #     return mpd 

    

    


           
# class DataAdmin(ImportMixin, admin.ModelAdmin):
#     resource_class = DataResource
#     form = DataForm
#     list_display = ("station", "tilting_date", "tilting_time", "tilting_number", "tilting_mm","valuetest","name")
#     readonly_fields=("valuetest",)

#     def get_import_form(self):
#         # Uncomment only if data is stored already in the database
#         print(MeanDay().calculate_mean_per_day) # Test to see if average works
#         return CustomImportForm
    
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
    


# class MeanDayAdmin(admin.ModelAdmin):
#     list_display = ("station","mean_day", "mean_per_day","mean_day_real", "mean_per_day_real")

#     @property
#     def testover(self):
#         meanday = MeanDay(station = Data.objects.last().station,
#                           mean_day = Data.objects.last().tilting_date)
#         self.mean_day.save()
#         return mean_day

    


           

# admin.site.register(Data, DataAdmin)
# admin.site.register(MeanDay,MeanDayAdmin)
# admin.site.register(MeanWeek)
# admin.site.register(MeanYear)
# admin.site.register(Intensity)

