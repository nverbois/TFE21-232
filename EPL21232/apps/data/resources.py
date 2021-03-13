from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, TimeWidget, DateWidget
from .models import Station, Data, Mean, Intensity

class DataResource (resources.ModelResource):

    station = fields.Field(
        column_name='station',
        attribute='station',
        widget=ForeignKeyWidget(Station, 'name'))

    tilting_time = fields.Field(
        column_name='tilting_time',
        attribute='tilting_time',
        widget=TimeWidget())

    tilting_date = fields.Field(
        column_name='tilting_date',
        attribute='tilting_date',
        widget=DateWidget())

    class Meta:
        model = Data
        fields = ('station','tilting_number','tilting_mm', 'tilting_date','tilting_time') #Select the field to import for the resource
        exclude = ('id',)
        import_id_fields = ('tilting_date', 'station',)
        export_order = ('station','tilting_number','tilting_mm', 'tilting_date','tilting_time')

        