from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [


    path('', views.tela_inicial, name='tela_inicial'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('cadastro/', views.cadastro, name='cadastro'),  # Cadastro
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inicial/', views.inicial, name='inicial'),
    path('criar_evento/', views.criar_evento, name='criar_evento'),
    path('listar_eventos/', views.listar_eventos, name='listar_eventos'),
    path('detalhes_evento/<int:evento_id>/', views.detalhes_evento, name='detalhes_evento'),
    path('editar_evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('excluir_evento/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('saiba_mais/', views.saiba_mais, name='saiba_mais'),
    path('suporte/', views.suporte, name='suporte'),
    path('quem_somos/', views.quem_somos, name='quem_somos')
    ]