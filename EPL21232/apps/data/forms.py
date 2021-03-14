from django import forms
from import_export.admin import ImportForm, ConfirmImportForm
from .models import Station

class CustomImportForm(ImportForm):
    station = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        required=True
    )

class CustomConfirmImportForm(ConfirmImportForm):
    station = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        required=True
    )