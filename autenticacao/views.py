from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm
from .models import Evento
from .forms import EventoForm
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import localtime

#TELA INICIAL PÓS CADASTRO
@login_required
def inicial(request):
    usuario = request.user

    # Obtendo a hora atual
    hora_atual = timezone.now()
    print("Hora atual:", hora_atual)

    # Busca o próximo evento do usuário (se houver)
    proximo_evento = Evento.objects.filter(horario_inicio__gt=hora_atual).order_by('horario_inicio').first()
    
    if proximo_evento:
        # Convertendo a hora para o fuso horário local
        horario_evento = localtime(proximo_evento.horario_inicio).strftime('%H:%M')
        mensagem_evento = f"seu próximo evento é às {horario_evento}."
    else:
        mensagem_evento = "sem eventos futuros."

    # Busca todos os eventos para exibir na lista
    eventos = Evento.objects.all()

    return render(request, 'autenticacao/inicial.html', {
        'usuario': usuario,
        'mensagem_evento': mensagem_evento,
        'eventos': eventos
    })

def tela_inicial(request):
    return render(request, 'autenticacao/tela_inicial.html')  # Altere para o template correto


@login_required
def dashboard(request):
    return render(request, 'autenticacao/tela_inicial.html')

# autenticacao/views.py
def cadastro(request):  # Mudando o nome para 'cadastro'
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'registration/cadastro.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicial')  # Certifique-se de que 'inicial' está no urls.py
        else:
            messages.error(request, "Usuário ou senha incorretos.")  # Mensagem de erro
    return render(request, 'autenticacao/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento criado com sucesso!")
            return redirect('listar_eventos')
        else:
            # Exibindo as mensagens de erro de validação
            messages.error(request, "Por favor, corrija os erros no formulário.")
            return render(request, 'eventos/criar_evento.html', {'form': form})
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

# Listar eventos com busca e filtros
@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()

    # Pegando os parâmetros da busca
    titulo = request.GET.get('titulo', '').strip()
    local = request.GET.get('local', '').strip()
    data = request.GET.get('data', '').strip()
    tipo = request.GET.get('tipo', '').strip()

    # Aplicando filtros
    if titulo:
        eventos = eventos.filter(titulo__icontains=titulo)
    
    if local:
        eventos = eventos.filter(local__icontains=local)

    if data:
        eventos = eventos.filter(horario_inicio__date=data)

    if tipo:
        eventos = eventos.filter(tipo_evento=tipo)

    # Verifica se há eventos após o filtro
    if not eventos.exists():
        mensagem = "Nenhum evento encontrado."
    else:
        mensagem = ""

    return render(request, 'eventos/listar_eventos.html', {
        'eventos': eventos,
        'titulo': titulo,
        'local': local,
        'data': data,
        'tipo': tipo,
        'mensagem': mensagem
    })

# Visualizar evento
def ver_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/ver_evento.html', {'evento': evento})

# Editar evento
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

# Excluir evento
def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        evento.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

#Detalhes do evento
def detalhes_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})


def calendar_view(request):
    return render(request, 'eventos/calendar.html') 

def saiba_mais(request):
    return render(request, 'autenticacao/saiba_mais.html')

def suporte(request):
    return render(request, 'autenticacao/suporte.html')

def quem_somos(request):
    return render(request, 'autenticacao/quem_somos.html')