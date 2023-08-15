from random import randint
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from functions.mixins import ContextMixin, ValidateUserDataRegister
from tasks.forms import TaskForm

class HomeView(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, TemplateView):
    template_name = 'home.html'
    custom_context = {
        'app_name': 'Mis tareas',
        'range_for': range(1, randint(1, 11))
    }

class NewTask(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, CreateView):
    template_name = 'new_task.html'
    form_class = TaskForm

    custom_context = {
        'app_name': 'Nueva tarea',
        'range_for': range(1, randint(1, 11))
    }

class TasksImportants(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, TemplateView):
    template_name = 'task_important.html'
    custom_context = {
        'app_name': 'Tareas importantes',
        'range_for': range(1, randint(1, 11))
    }

class TasksPending(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, TemplateView):
    template_name = 'task_basic.html'
    custom_context = {
        'app_name': 'Tareas basicas',
        'range_for': range(1, randint(1, 11))
    }

class TasksPostponed(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, TemplateView):
    template_name = 'task_postponed.html'
    custom_context = {
        'app_name': 'Tareas pospuestas',
        'range_for': range(1, randint(1, 11))
    }

class TasksIncomplete(LoginRequiredMixin, ValidateUserDataRegister, ContextMixin, TemplateView):
    template_name = 'task_incomplete.html'
    custom_context = {
        'app_name': 'Tareas incompletas',
        'range_for': range(1, randint(1, 11))
    }