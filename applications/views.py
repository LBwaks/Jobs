from django.shortcuts import render
from applications.forms import ApplicationForm
from applications.models import Application,Job
from.forms import ApplicationForm
from django.urls.base import reverse_lazy ,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,get_object_or_404
# Create your views here.
class ApplicationView(ListView):
    model = Application
    template_name = 'applications/application.html'
    queryset = Application.objects.all()

class ApplicationDetailView(DetailView):
    model = Application
    template_name ='applications/application_details.html'

    def  get_context_data(self, *args,**kwargs):
        return super(ApplicationView,self).get_context_data(**kwargs)
        # context[""] = 
        # return context

class AddApplicationView(CreateView):
    model =Application
    form_class=ApplicationForm
    template_name ='applications/add_application.html'
    # job = get_object_or_404(Job, id=job_id)
    # j = get_object_or_404(Event, slug=slug)
    
    def form_valid(self,form):        
        # job = get_object_or_404(Job, slug=self.kwargs['slug'])       
        application =form.save(commit=False)
        application.user = self.request.user
        # pk = self.kwargs['job_id']
        # application.instance.job = self.kwargs.get('id')
        # application.instance.job = self.request.job
        # application.save()
        # application.save_m2m()
        return super(AddApplicationView,self).form_valid(form)

    # def form_valid(self,form):
    #     job =form.save(commit=False)
    #     form.job = job
    #     job.save()
    #     form.save_m2m()
    #     return super().form_valid(form)



    # if form.is_valid():
    # profile = form.save(commit=False)
    # profile.ip_address = request.META['REMOTE_ADDR']
    # profile.user = request.user
    # profile.save()
    # return redirect('profile')