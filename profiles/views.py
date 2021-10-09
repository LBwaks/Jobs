from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import PersonalForm, LocationForm, SeekerForm
from .models import Personal

# Create your views here.
class Multistepformsubission(SessionWizardView):
    template_name = 'profiles/profile.html'
    form_list = [PersonalForm,LocationForm,SeekerForm]

    def done(self, form_list,form_dict, **kwargs):
        form_data= [form.cleaned_data for form in form_list]
        form_dict = self.get_all_cleaned_data()
        # personal = Personal()
        personal = Personal.objects.create(**form_dict,user=self.request.user,)
        personal.save()
        # personaldata = form_dict['personal'].save()
        # seeker = form_dict['seeker'].save()
        # location =form_dict['location'].save()
        return render(self.request, 'pages/home.html', {
            'data':form_data
        })