from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='cbv/about.html'), name='about'),       
    path('team/', TeamView.as_view(), name='team'),       
]