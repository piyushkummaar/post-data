from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView


class TeamView(View):
    def get(self,requset):
        return HttpResponse('<h1>Hello World!!</h1>')
    
class Home(TemplateView):
    template_name = 'cbv/first_cbv.html'
    def get_context_data(self,*args,**kwargs):
        context = super(Home,self).get_context_data(**kwargs)
        context['title'] = 'home page'
        return context
    
