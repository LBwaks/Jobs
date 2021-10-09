from django import forms
from .models import Personal, Location, Seeker
from phonenumber_field.modelfields import PhoneNumberField

class PersonalForm(forms.ModelForm):
    class Meta :
        model = Personal
        fields = ('user_type','id_passport','email','phone_number','gender','bio','profile_pic')

class LocationForm(forms.ModelForm):
    class Meta :
        model = Location
        fields = ('location_county','location_town','location_location','location_address')

class SeekerForm(forms.ModelForm):
    class Meta :
        model : Seeker 
        fields =('skills','good_conduct','certificates','id_front','id_back')
