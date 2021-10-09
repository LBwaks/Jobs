from django.urls import path
from .import views
from .views import JobDetailView, JobView, AddJobView,UpdateJobView,ApproveApplication

urlpatterns = [
    path('',JobView.as_view(), name="jobs"),
    path('<slug>',JobDetailView.as_view(),name='job_details'),
    path('add_job/',AddJobView.as_view(),name='add_job'),
    path('edit/<slug>',UpdateJobView.as_view(),name="update_job"),
    path('<job_slug><application_application_uuid>', ApproveApplication.as_view(),name="approve"),
]
