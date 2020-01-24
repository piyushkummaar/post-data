from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('delete/<int:pk>', delete, name='delete'),
    path('<int:pk>/edit', update, name='update'),
    path('details/<int:pk>', details,name='details'),
    path('create/', create, name='create'),


]
