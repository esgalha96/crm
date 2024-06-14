from django.forms import ModelForm, PasswordInput
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "password", "phone_number"]
        widgets = {
            'password': PasswordInput(),
        }