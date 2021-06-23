from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Estacionamiento

class UserRegistroForm(UserCreationForm):
    email = forms.EmailField()
    password1 =forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 =forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

class EstacionamientoForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Describe el estacionamiento'}), required=True)

    class Meta:
        model = Estacionamiento
        fields = ['content']