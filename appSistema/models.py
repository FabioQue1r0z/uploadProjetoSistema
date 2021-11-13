from django.db import models

# Create your models here.

class Cardapio(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    preco = models.DecimalField('Preço:', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
