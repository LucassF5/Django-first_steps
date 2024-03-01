from django.urls import path
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path("login", login, name="login"),
    path("cadastro",cadastro, name="cadastro"),
    path("logout", logout, name="logout")
]

# path("nome_da_url", nome_da_view, name="nome_da_url)