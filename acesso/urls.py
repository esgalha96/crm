from django.urls import path
from .views import login_acesso, cadastro, logout_acesso

urlpatterns = [
    path('', login_acesso, name='login_acesso'),
    path('logout/', logout_acesso, name='logout_acesso'),
    path('cadastro/', cadastro, name='cadastro'),
]
