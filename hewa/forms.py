from django import forms
from .lookups import StationLookup #lookups comes from selectable
from .models import Station
from selectable import forms as selectable_forms

# validation for station form input
class StationForm(forms.Form):
	autocomplete = forms.CharField(label='Type the name of station',
					widget=selectable_forms.AutoCompleteWidget(StationLookup),
					required=False)

#validation for the upload
class UploadForm(forms.Form):
	identifier = forms.CharField(required=True)
	carbonmonoxide_sensor_reading = forms.DecimalField(required=True)
	nitrogendioxide_sensor_reading = forms.DecimalField(required=True)
	lpg_gas_sensor_reading = forms.DecimalField(required=True)
