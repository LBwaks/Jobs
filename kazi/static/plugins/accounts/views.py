from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import PersonalForm,LocationForm,SeekerForm

# Create your views here.
class Multistepformsubission(SessionWizardView):
    template_name = 'profiles/profile.html'
    form_list = [PersonalForm,LocationForm,SeekerForm]

    def done(self, form_list, **kwargs):
        form_data= [form.cleaned_data for form in form_list]
        return render(self.request, 'pages/home.html', {
            'data':form_data
        })