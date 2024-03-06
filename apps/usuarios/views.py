from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()  # Instancia o formulário

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(  # Autentica o usuário
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:  # Se o usuário existe
                auth.login(request, usuario)
                messages.success(request, f"{nome} está logado com sucesso")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')

    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':  # Verifica se o método é POST
        form = CadastroForms(request.POST)

        if form.is_valid():
                    #    SENHAS VALIDADAS NO FORMS.PY
            # if form['senha_1'].value() != form['senha_2'].value():
            #     messages.error(request, "As senhas não são iguais")
            #     # Redireciona para a página de cadastro
            #     return redirect("cadastro")

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            # Verifica se o usuário já existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente")
                return redirect("cadastro")
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email já existente")
                return redirect("cadastro")

            usuario = User.objects.create_user(  # Cria um usuário
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()  # Salva o usuário
            messages.success(request, "Cadastro com sucesso")
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect("login")

# The views are the functions that will be called when the user accesses the URL.
# The function receives a request object and returns a response object.
# In this case, the response is the HTML page that will be displayed to the user.
# The render function receives the request object and the name of the HTML file that will be rendered.
# The HTML files are located in the templates folder of the application.
# The render function returns a response object with the HTML content.

# render(request, "template/arquivo.html")
