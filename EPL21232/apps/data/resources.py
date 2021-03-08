from import_export import resources
from .models import Station, Data, Mean, Intensity

class DataResource (resources.ModelResource):
    class Meta:
        model = Data