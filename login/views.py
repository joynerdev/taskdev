from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView

from functions.mixins import ContextMixin, IsUserAunthenticated, RestrictSecondPageRegister
from .forms import RegisterProfileForm, SecondStepRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Vista de Inicio de Sesion
class SignInView(ContextMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    custom_context = {
        'app_name': 'Iniciar Sesion'
    }

class SignOutView(LoginRequiredMixin, LogoutView):
    pass

class RegisterProfile(IsUserAunthenticated, ContextMixin, CreateView):
    form_class = RegisterProfileForm
    success_url = reverse_lazy('login:dataProfile')
    template_name = 'register.html'
    custom_context = {
        'app_name': 'Registrar nuevo usuario'
    }
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class SecondDataProfile(LoginRequiredMixin, RestrictSecondPageRegister, ContextMixin, UpdateView):
    form_class = SecondStepRegisterForm
    template_name = "data_profile.html"

    success_url = reverse_lazy('login:dataProfile')

    custom_context = {
        'app_name': 'Finalizar registro de perfil',
        'title_container': 'Ultimos ajustes a tu perfil 👷'
    }

    def get_object(self):
        return self.request.user