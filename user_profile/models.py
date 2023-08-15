import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image #type:ignore

# Se hereda de la base del modelo usuario, reescribiendo el modelo que tiene por defecto
# django

def get_image_path(instance, filename):
    # Genera un UID único
    uid = uuid.uuid4()
    # Obtiene la extensión original del archivo
    extension = os.path.splitext(filename)[1]
    # Define la nueva ruta del archivo de la imagen con el UID como nombre y la extensión original
    new_filename = f'profile_img/{uid}{extension}'
    return new_filename


class User(AbstractUser):
    image = models.ImageField(verbose_name="Imagen de perfil", upload_to=get_image_path, blank=True)
    nick = models.CharField(verbose_name="Apodo", max_length=50, blank=True)
    bio = models.TextField(verbose_name="Descripcion o motivos de registro", blank=True)

    class Meta:
        db_table = "user"
        managed = True
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["id"]

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)
            max_size = (400, 400)
            image.thumbnail(max_size, Image.LANCZOS)
            image.save(self.image.path, quality=10, optimize=True)