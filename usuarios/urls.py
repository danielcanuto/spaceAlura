from django.urls import path
from usuarios.views import login, cadastro, logout


urlpatterns = [
    path("login", login, name='login'),
    path("cadastro", cadastro, name='cadastro'),
    path("logtou", logout, name='logout'),
]