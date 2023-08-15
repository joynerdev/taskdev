from django.forms import ModelForm

from tasks.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_limit', 'task_priority', 'task_image', 'task_description']
        