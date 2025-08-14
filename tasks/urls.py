from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('<int:pk>/toggle/', views.task_toggle, name='toggle'),
    path('<int:pk>/edit/', views.task_edit, name='edit'),
    path('<int:pk>/delete/', views.task_delete, name='delete'),
    path('cadastro/', views.cadastro_usuario,name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tasks:login'), name='logout'),
]