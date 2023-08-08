from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

# Para restringir el acceso a la segunda pagina de registro de usuario se crea este mixin
class RestrictSecondPageRegister(UserPassesTestMixin):
    def test_func(self):
        # Tomamos como referencia el nombre del usuario si esta en blanco el perfil es nuevo
        return True if self.request.user.first_name == '' else False

    def handle_no_permission(self):
        return redirect('home:home')