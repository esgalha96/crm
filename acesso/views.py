from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

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
    return render(request, 'cadastro.html')