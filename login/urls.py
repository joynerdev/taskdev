from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('', SignInView.as_view(), name='loginProfile'),
    path('register', RegisterProfile.as_view(), name='newProfile'),
    path('finish', SecondDataProfile.as_view(), name='dataProfile'),
    
]
