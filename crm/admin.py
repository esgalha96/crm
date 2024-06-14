from django.contrib import admin
from .models import Cliente, Empreendimento, Movimentacao, Ocorrencia, Status

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empreendimento)
admin.site.register(Status)
admin.site.register(Ocorrencia)
admin.site.register(Movimentacao)