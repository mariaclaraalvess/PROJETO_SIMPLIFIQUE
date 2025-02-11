from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento  # Modelo Evento, que você criou nas migrações
        fields = ['titulo', 'descricao', 'data', 'horario_inicio', 'local', 'tipo_evento']
        

class CadastroForm(UserCreationForm):
    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Telefone'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'User'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Crie uma senha'}),
    label="Senha"
    )
    password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
    label="Senha"
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefone', 'password1', 'password2']


