from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)
        
        if form.is_valid():
            name=form["nome_login"].value()
            senha=form["senha"].value()

        usuario= auth.authenticate(
            username=name,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"✔ Seja bem vindo, \n{name.upper()} 👍🏿")
            return redirect('index')
        else:
            messages.error(request, "⚠  Erro!! verifique login e senha ⚠")
            return redirect('login')

    return render(request, 'usuarios/login.html',{"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "⚠ Verifique se as senhas são iguais ⚠")
                return redirect('cadastro')

            name=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, f'⚠ O usuário "{name}" já existe, tente outro nome ⚠')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=name,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return(redirect('login'))


    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):

    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('index')