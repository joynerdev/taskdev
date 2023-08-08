from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from functions.mixins import ValidateUserDataRegister

class HomeView(LoginRequiredMixin, ValidateUserDataRegister, TemplateView):
    template_name = 'home.html'
