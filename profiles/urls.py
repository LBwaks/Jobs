from django.urls import path
from .import views
from .views import Multistepformsubission

urlpatterns = [
    path('profile',Multistepformsubission.as_view(), name="profile_form"),
    
]
#