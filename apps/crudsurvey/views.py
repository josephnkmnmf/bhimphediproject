from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

from apps.crudsurvey.models import Surve
from apps.crudsurvey.forms import SurveForm
from apps.crudsurvey.filters import SurveFilter

#for login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
#from django.template.context_processors import csrf
from django.contrib import auth

# Create your views here.
# @login_required(login_url="/survey/login/")
class SurveCreate(CreateView):
    model = Surve
    form_class = SurveForm
    template_name = 'crudsurvey/survey_form.html'
    success_url = reverse_lazy('survey:Surve_list')

class SurveList(ListView):
    queryset = Surve.objects.order_by('ref_no')
    template_name = 'crudsurvey/surve_list.html'
    paginate_by = 4

class SurveUpdate(UpdateView):
    model = Surve
    form_class = SurveForm
    template_name = 'crudsurvey/survey_form.html'
    success_url = reverse_lazy('survey:Surve_list')

class SurveDelete(DeleteView):
    model = Surve
    template_name = 'crudsurvey/surve_delete.html'
    success_url = reverse_lazy('survey:Surve_list')

class SurveShow(DetailView):
    model = Surve
    template_name = 'crudsurvey/surve_show.html'

def search(request):
    Surve_list = Surve.objects.all()
    Surve_filter = SurveFilter(request.GET, queryset=Surve_list)
    return render(request, 'crudsurvey/surve_list2.html', {'filter': Surve_filter})

#for login

@login_required
def login(request):
    return render_to_response('crudsurvey/login.html', {'user': request.user})

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/survey/new')
    else:
        return HttpResponseRedirect('/survey/invalid')

def loggedin(request):
    return render_to_response('crudsurvey/loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('crudsurvey/invalid_login.html')

def logout(request):
    auth.logout(request)
    #return HttpResponseRedirect('/')
    return render_to_response('crudsurvey/login.html')

