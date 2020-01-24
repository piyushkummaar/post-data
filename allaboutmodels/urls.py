from django.urls import path
from .views import allaboutmodels

urlpatterns = [
    path('allaboutmodels/', allaboutmodels, name='models')
]
