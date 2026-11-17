from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Venda(models.Model):
    FORMA_PAGAMENTO = [
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
        ('Fiado', 'Fiado'),
    ]
    data_hora = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Venda {self.id} - R$ {self.valor_total}"