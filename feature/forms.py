import datetime
from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('entered_by', 'feature', 'desc', 'bid')
        labels = {
            'entered_by':'Your Name',
            'feature':'Feature',
            'desc':'Detailed Feature Description',
            'bid':'Your Bid'
            }
