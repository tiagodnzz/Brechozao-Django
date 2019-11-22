from django.db import models

# Create your models here.

class Produto(models.Model):
    opcoes_tamanho = [
        ('PP', 'Extra pequeno'),
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande'),
    ]


    nome = models.CharField(max_length=50)
    preco =  models.DecimalField(decimal_places=2, max_digits=1000, default=50)
    disponivel = models.BooleanField(default=True)
    quantidade = models.IntegerField(default=1)
    tamanho = models.CharField(max_length=2, choices=opcoes_tamanho)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    metodo_pagamento = [
        ('AV', 'Pagamento à vista'),
        ('P2', 'Pagamento em 2x'),
        ('P3',  'Pagamento em 3x'),
    ]
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=metodo_pagamento)

    def __str__(self):
        return self.nome