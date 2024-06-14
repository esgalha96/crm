from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.hashers import make_password

# Create your views here.
def login_acesso(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Usuário e senha incorretos!")

    return render(request, 'login.html')

def logout_acesso(request):
    logout(request)
    return redirect('login_acesso')

def cadastro(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = UsuarioForm()

    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)