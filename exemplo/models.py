from django.db import models
from django.forms import CharField

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Programador(models.Model):
    nome = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.nome        
