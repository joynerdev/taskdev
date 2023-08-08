from django import forms
from user_profile.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label="Nombre de usuario")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Contraseña")

class RegisterProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SecondStepRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'nick', 'bio']

        # Se reemplaza el TextArea por un campo de texto normal
        widgets = {
            'bio': forms.TextInput(),
        }