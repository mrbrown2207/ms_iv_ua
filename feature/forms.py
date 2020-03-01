import datetime
from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):
    """Feature request form"""
    class Meta:
        model = Feature
        fields = ('feature', 'desc')
        labels = {
            'feature':'Feature *',
            'desc':'Detailed Feature Description *',
        }
        widgets = {
            'feature':forms.TextInput(attrs={
                'class':'form-control ua-required',
                'aria-describedby':'feature title',
                'placeholder':'Feature title',
                'minlength':'1',
                'maxlength':'80',
            }),
            'desc':forms.Textarea(attrs={
                'class':'form-control ua-required char-countdown',
                'aria-describedby':'feature description',
                'placeholder':'Enter detailed feature description',
                'cols':70, 'rows':10,
                'minlength':'1',
                'maxlength':'1000',
            }),
        }
