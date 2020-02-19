from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('entered_by', 'subj', 'desc')
        labels = {
            'entered_by':'Your Name',
            'subj':'Bug Title',
            'desc':'Detailed Description'
            }
