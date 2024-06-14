from django.db import models
from datetime import datetime as dt

class Status(models.Model):
    status = models.CharField(max_length=50, verbose_name="Status")
    ordem = models.IntegerField(verbose_name="Ordem")

    def __str__(self):
        return self.status

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")
    email = models.CharField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.nome
    
class Empreendimento(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    numero_unidades = models.IntegerField(verbose_name="Número UHs")

    def __str__(self):
        return f"{self.nome} ({self.numero_unidades})"
    
class Ocorrencia(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.PROTECT, verbose_name="Cliente")
    empreendimento = models.ForeignKey("Empreendimento", on_delete=models.PROTECT, verbose_name="Empreendimento")
    operador_responsavel = models.ForeignKey("acesso.Usuario", on_delete=models.PROTECT, verbose_name="Operador Responsável")

    def __str__(self):
        return f"(OC {self.pk}) {self.cliente}"
    
    class Meta:
        ordering = ["pk", "cliente"]
    
class Movimentacao(models.Model):
    ocorrencia = models.ForeignKey("Ocorrencia", on_delete=models.PROTECT, related_name="movimentacoes")
    comentario = models.TextField(verbose_name="Comentário")
    operador_responsavel = models.ForeignKey("acesso.Usuario", on_delete=models.PROTECT, verbose_name="Operador Responsável")
    status = models.ForeignKey("Status", on_delete=models.PROTECT, verbose_name="Status")
    data = models.DateField(default=dt.now())

    def __str__(self):
        return f"{self.ocorrencia} - {self.pk}"
    
    class Meta:
        ordering = ["ocorrencia", "pk"]