from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import RegisterProfileForm


class RegisterProfile(TemplateView):
    template_name = 'register.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_register"] = RegisterProfileForm()
        context["app_name"] = 'Nuevo Usuario'
        return context


class SecondDataProfile(TemplateView):
    template_name = "data_profile.html"