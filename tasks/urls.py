from django.urls import path
from .views import *

app_name = 'task'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('importantes', TasksImportants.as_view(), name='important'),
    path('basicas', TasksPending.as_view(), name='basic'),
    path('pospuestas', TasksPostponed.as_view(), name='postponed'),
    path('incompletas', TasksIncomplete.as_view(), name='incomplete'),
    path('nueva', NewTask.as_view(), name='new')
    
]
