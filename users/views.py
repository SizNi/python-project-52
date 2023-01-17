from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from users.models import CustomUser


class IndexView(TemplateView):
    
    template_name = 'users.users.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        print(context)
        return render(
            request,
            template_name = 'users.html',
            context = {
                'users': CustomUser.objects.all(),
                'title': 'Users'
            }
        )
