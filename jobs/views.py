from django.shortcuts import get_object_or_404, render
from django .views.generic import ListView,DetailView,CreateView,UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from applications.models import Application
from jobs.forms import JobForm ,JobEditForm
from .models import Job
from django.urls.base import reverse_lazy,reverse
# Create your views here.

class JobView(ListView):
    model = Job 
    template_name ='jobs/jobs.html'
    queryset = Job.objects.all()


class JobDetailView(DetailView):
    model =Job 
    template_name ='jobs/job-details.html'

    def get_context_data(self,*args, **kwargs):
        context= super(JobDetailView,self).get_context_data(**kwargs)
        job = get_object_or_404(Job,slug=self.kwargs['slug'])
        applications= Application.objects.filter(job=job).order_by('created_at')
        context['job'] =job
        context['applications'] = applications
        return context

class AddJobView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/add_job.html'

    def form_valid(self,form):
        job =form.save(commit=False)
        form.instance.user = self.request.user
        job.save()
        form.save_m2m()
        return super().form_valid(form)


class UpdateJobView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model =Job 
    form_class=JobEditForm
    template_name ='jobs/update_job.html'

class ApproveApplication(View):
    def get(self):
     job = get_object_or_404(Job, slug = self.kwargs['slug'])
     application =Application.objects.filter(job=job)
     application.status ='Approved'
     application.save()

