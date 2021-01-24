from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nome=models.CharField(max_length=255)

    def __str__(self):
        return self.nome



class Contato(models.Model):
    #criar os campos
    nome=models.CharField(max_length=255)  #limitar o tamanho do nome
    sobrenome=models.CharField(max_length=255, blank=True)  # porque o sobrenome e opcional
    telefone=models.CharField(max_length=255)
    email=models.CharField(max_length=255, blank=True)
    data_criacao=models.DateTimeField(default=timezone.now)
    descricao=models.TextField(blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)  # relaciona a tabela aqui cm a debaixo
    # caso a categoria seja apaga, nao apaga o resto

    def __str__(self):
        return self.nome
