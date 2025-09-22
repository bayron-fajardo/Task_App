from django.urls import path
from .views import *

app_name = 'task_app'

urlpatterns = [
    path('', HomeView, name='home'),
]