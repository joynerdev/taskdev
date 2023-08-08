from django.views.generic import TemplateView

from functions.mixins import ValidateUserDataRegister

class HomeView(ValidateUserDataRegister, TemplateView):
    template_name = 'welcome.html'
