from django.urls import path 
from .views import ApplicationView,ApplicationDetailView,AddApplicationView

urlpatterns = [
    path('',ApplicationView.as_view(),name='applications'),
    path('<profile_uuid>',ApplicationDetailView.as_view(),name='application-details'),
    path('apply_job/<job_slug>',AddApplicationView.as_view(),name="apply_job")
]
