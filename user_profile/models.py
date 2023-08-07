from django.db import models
from django.contrib.auth.models import AbstractUser

# Se hereda de la base del modelo usuario, reescribiendo el modelo que tiene por defecto
# django
class User(AbstractUser):
    image = models.ImageField(verbose_name="Imagen de perfil", upload_to="profile_img")
    nick = models.CharField(verbose_name="Apodo", max_length=50)
    bio = models.TextField(verbose_name="Descripcion o motivos de registro")
