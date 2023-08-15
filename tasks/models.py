import os
import uuid
from django.db import models
from PIL import Image #type:ignore

from user_profile.models import User

def get_image_path(instance, filename):
    # Genera un UID único
    uid = uuid.uuid4()
    # Obtiene la extensión original del archivo
    extension = os.path.splitext(filename)[1]
    # Define la nueva ruta del archivo de la imagen con el UID como nombre y la extensión original
    new_filename = f'tasks_images/{uid}{extension}'
    return new_filename

class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre de la tarea')
    date_register = models.DateTimeField(verbose_name='Fecha registro', auto_now_add=True)
    date_limit = models.DateTimeField(verbose_name='Fecha limite')
    times_postponed = models.IntegerField(verbose_name='Veces pospuesta')
    task_priority = models.CharField(verbose_name='Prioridad de la tarea', max_length=50)
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    task_image = models.ImageField(verbose_name="Imagen de la tarea (Opcional)", upload_to=get_image_path, blank=True)
    task_description = models.TextField(verbose_name='Descripcion de la tarea')

    class Meta:
        db_table = "task"
        managed = True
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["id"]
