from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

# Para restringir el acceso a la segunda pagina de registro de usuario se crea este mixin
class RestrictSecondPageRegister(UserPassesTestMixin):
    def test_func(self):
        # Tomamos como referencia el nombre del usuario si esta en blanco el perfil es nuevo
        return True if self.request.user.first_name == '' else False

    def handle_no_permission(self):
        return redirect('home:home')
    
# Para validar que los datos del usuario esten completos se usa este mixin
# Si no estan completos se redirige a la vista de completado de datos
class ValidateUserDataRegister(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.first_name == '': return False
        else: return True

    def handle_no_permission(self):
        return redirect('login:dataProfile')
    
# Verifica si el usuario esta autenticado, si lo esta redirige a la vista principal
class IsUserAunthenticated(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    def handle_no_permission(self):
        return redirect('home:home')

"""
    Mixin encargado de agregar datos al contexto de forma facil, sin reescribir en la vista el
    metodo get_context

    trabaja con una propiedad llamada custom_context
 """   
class ContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # type: ignore
        
        # Valida si la propiedad esta registrada en la clase
        if hasattr(self, 'custom_context'):
            # Se recorre el diccionario que esta dentro de la propiedad de la clase
            for key, value in self.custom_context.items():
                # Se asigna al cotexto
                context[key] = value 
        # Si no se encuentra la propiedad se envia una alerta
        else:
            # Se crea una variable donde se guardan las rutas de las clases
            clases = ''

            # Se recorren las clases bases
            for base in self.__class__.__bases__:
                # Se guardan en la variable, se concatenan
                clases += f"{base.__name__} > "

            # Se imprime en la consola
            print(f"#*#*#*#*#*#*#*#*#*#*#*#*#* No se esta usando el context mixin {clases} #*#*#*#*#*#*#*#*#*#*#*#*#*")

        # Devuelve el contexto  
        return context