from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, TimeWidget, DateWidget
from .models import Station, Data, MeanDay, Intensity

class DataResource (resources.ModelResource):

    station = fields.Field(
        column_name='station',
        attribute='station',
        widget=ForeignKeyWidget(Station, 'name'))

    heure = fields.Field(
        column_name='heure',
        attribute='heure',
        widget=TimeWidget())

    date = fields.Field(
        column_name='date',
        attribute='date',
        widget=DateWidget())

    class Meta:
        model = Data
        fields = ('station','mesure', 'date','heure') #Select the field to import for the resource
        exclude = ('id',)
        import_id_fields = ('date', 'heure', 'station')
        export_order = ('station','mesure', 'date','heure')

        