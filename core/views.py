from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponse

# Create your views here.
class HomePageView(TemplateView):    
    template_name='core/basico.html'


    """def get(self, request, *args, **kwargs):    
        return HttpResponse("PAGINA BASICA ")
    """