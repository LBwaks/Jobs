from django import forms
from django.forms import fields, widgets 
from .models import Application, Job
from ckeditor.widgets import CKEditorWidget

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application 
        fields =('charge','job','other_description')

        labels ={
            'charge':'Charge',
            'other_description':'Other Offer'
        }

        widgets ={
            'charge':forms.TextInput(attrs={'class':'form-control' 'required'}),
            'other_description': forms.CharField(widget=CKEditorWidget()),
        }