from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Tipo(models.Model):
	tipo = models.CharField(max_length=25)

	def __str__(self):
   		return self.tipo


class Post(models.Model):
    usuario = models.ForeignKey('auth.User')
    tipo_transacao = models.ForeignKey('Tipo')
    data = models.DateField(("Date"))
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
   		return self.descricao