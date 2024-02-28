from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms() # Instancia o formulário
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})

# The views are the functions that will be called when the user accesses the URL.
# The function receives a request object and returns a response object.
# In this case, the response is the HTML page that will be displayed to the user.
# The render function receives the request object and the name of the HTML file that will be rendered.
# The HTML files are located in the templates folder of the application.
# The render function returns a response object with the HTML content.

# render(request, "template/arquivo.html")