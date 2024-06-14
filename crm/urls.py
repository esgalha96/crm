from django.urls import path
from .views import home, add_ocorrencia

urlpatterns = [
    path('', home, name='home'),
    path('ocorrencias/add/', add_ocorrencia, name='add_ocorrencia'),
]
