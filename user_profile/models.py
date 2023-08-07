from django.db import models
from django.contrib.auth.models import AbstractUser

# Se hereda de la base del modelo usuario, reescribiendo el modelo que tiene por defecto
# django
class User(AbstractUser):
    image = models.ImageField(verbose_name="Imagen de perfil", upload_to="profile_img", blank=True)
    nick = models.CharField(verbose_name="Apodo", max_length=50, blank=True)
    bio = models.TextField(verbose_name="Descripcion o motivos de registro", blank=True)

    class Meta:
        db_table = "user"
        managed = True
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["id"]

    def __str__(self):
        return self.name