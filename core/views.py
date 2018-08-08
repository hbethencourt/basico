from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
import sys

# Create your views here.
@method_decorator(login_required ,name='dispatch')
class HomePageView(TemplateView):    
    template_name='core/basico.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)                  
        context["version"]=sys.version
        return context

