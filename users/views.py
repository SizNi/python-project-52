from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    
    template_name = 'users.users.html'
    
    def get(self, request, *args, **kwargs):
        
        pass
