from django import forms
from .lookups import StationLookup #lookups comes from selectable
from .models import Station
from selectable import forms as selectable_forms


class StationForm(forms.Form):
	autocomplete = forms.CharField(label='Type the name of station',
					widget=selectable_forms.AutoCompleteWidget(StationLookup),
					required=False)