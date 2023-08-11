from django import forms
from now_app import models as now_models
from django_select2 import forms as s2forms

class MuseumWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'museum__icontains',
        'institution__icontains',
    ]

class ComMuseumForm(forms.ModelForm):
    class Meta:
        model = now_models.ComMuseumList
        # fields = '__all__'
        fields = ['museum', 'institution']
        # widgets: {
        #     'nowlocality_set': NowMuseumWidget
        # }

class NowLocalityForm(forms.ModelForm):
    class Meta:
        model = now_models.NowLocality
        fields = ['museum']
        widgets = {
            'museum': MuseumWidget
        }

class NowSpeciesForm(forms.ModelForm):
    class Meta:
        model = now_models.ComSpecies
        fields = '__all__'

class NowReferenceForm(forms.ModelForm):
    class Meta:
        model = now_models.RefReference
        fields = '__all__'
