from django import forms
from .models import Personal
from phonenumber_field.modelfields import PhoneNumberField

class PersonalForm(forms.ModelForm):
    class Meta :
        model = Personal
        fields = ('user_type','id_passport','email','gender','bio')


class LocationForm(forms.ModelForm):
    class Meta :
        model = Personal
        fields = ('location_county','location_town','location_location','location_address')


class SeekerForm(forms.ModelForm):
    class Meta :
        model = Personal
        fields =('skills',)

