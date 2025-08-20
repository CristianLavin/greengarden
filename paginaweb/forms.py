from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'username', 'correo_electronico', 'password']
