from django import forms 
from .models import Job
from ckeditor.widgets import CKEditorWidget
import datetime
# from django.core.validators

class JobForm(forms.ModelForm):
    class Meta:
        model =Job
        fields =('title','tag','description',
        'done_by_date','done_at_date','location_county',
        'location_town','location_address_location',
        'location_exact_job_location','job_reference',
        'status','image','video')

        labels ={
            'title':'Job Title :',
            'tag': 'Job Tag :',
            'description':'Job Description :',            
            'done_by_date': 'Job Done By Date :',
            'done_at_date': 'Job Done At Date :',
            'location_county': 'County :',
            'location_town': 'Town :',
            'location_address_location': 'Location :',
            'location_exact_job_location': 'Address :',
            'job_reference': 'Job Reference :',
            # 'status':
            'image': 'Job Image :',
            'video':'Job Video :',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'tag': forms.Select(attrs={'class':'form-select'}),
            'description': forms.CharField(widget=CKEditorWidget()),
            'done_by_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'done_at_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'location_county': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_town': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_address_location': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_exact_job_location': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'job_reference': forms.TextInput(attrs={'class':'form-control' 'required'}),
            # 'status':
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'video':forms.FileInput(attrs={'class':'form-control'}),
        }


class JobEditForm(forms.ModelForm):
    class Meta:
        model =Job
        fields =('title','tag','description',
        'done_by_date','done_at_date','location_county',
        'location_town','location_address_location',
        'location_exact_job_location','job_reference',
        'status','image','video')

        labels ={
            'title':'Job Title :',
            'tag': 'Job Tag :',
            'description':'Job Description :',            
            'done_by_date': 'Job Done By Date :',
            'done_at_date': 'Job Done At Date :',
            'location_county': 'County :',
            'location_town': 'Town :',
            'location_address_location': 'Location :',
            'location_exact_job_location': 'Address :',
            'job_reference': 'Job Reference :',
            # 'status':
            'image': 'Job Image :',
            'video':'Job Video :',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'tag': forms.Select(attrs={'class':'form-select'}),
            'description': forms.CharField(widget=CKEditorWidget()),
            'done_by_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'done_at_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder': 'Select a date','type': 'datetime-local' }),
            'location_county': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_town': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_address_location': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'location_exact_job_location': forms.TextInput(attrs={'class':'form-control' 'required'}),
            'job_reference': forms.TextInput(attrs={'class':'form-control' 'required'}),
            # 'status':
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'video':forms.FileInput(attrs={'class':'form-control'}),
        }
