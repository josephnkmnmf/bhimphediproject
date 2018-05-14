from django import forms
from apps.crudsurvey.models import Surve

class SurveForm(forms.ModelForm):
    class Meta:
        model = Surve
        fields= [
            'ref_no',
            'house_owner',
            'phone_no',
            'longitude',
            'latitude',
        ]

        labels = {
            'ref_no':'Reference Num',
            'house_owner':'House Owners Name',
            'phone_no':'Phone No',
            'longitude':'Longitude',
            'latitude':'Latitude',

        }

        widgets={
            'ref_no': forms.TextInput(attrs={'class':'form-control'}),
            'house_owner': forms.TextInput(attrs={'class':'form-control'}),
            'phone_no': forms.TextInput(attrs={'class':'form-control'}),
            'longitude': forms.TextInput(attrs={'class':'form-control'}),
            'latitude': forms.TextInput(attrs={'class':'form-control'}),

        }