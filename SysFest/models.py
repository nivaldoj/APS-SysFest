# -*- coding: utf-8 -*-

from django.db import models
from django.utils import formats
from datetime import datetime

import locale

# Define o local pra PT-BR, para as datas do __unicode__
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Enumerations 
ENUM_SEXO = (
	('Masculino', 'Masculino'),
	('Feminino', 'Feminino'),
    ('Indefinido', 'Indefinido'),
)

ENUM_ESTADO = (
    ('Paraiba', 'Paraiba'),
    ('Pernambuco', 'Pernambuco'),
    ('Rio Grande do Norte', 'Rio Grande do Norte'),
    ('Ceara', 'Ceara'),
    ('Alagoas', 'Alagoas'),
    ('Sergipe', 'Sergipe'),
    ('Bahia', 'Bahia'),
    ('Piaui', 'Piaui'),
    ('Maranhao', 'Maranhao'),
)

ENUM_COR = (
    ('Azul', 'Azul'),
    ('Amarelo', 'Amarelo'),
    ('Verde', 'Verde'),
    ('Laranja', 'Laranja'),
    ('Rosa', 'Rosa'),
    ('Roxo', 'Roxo'),
    ('Vermelho', 'Vermelho'),
    ('Cinza', 'Cinza'),
    ('Preto', 'Preto'),
    ('Branco', 'Branco'),
    ('Marrom', 'Marrom'),
)

ENUM_TIPO_PAGAMENTO = (
    ('Dinheiro', 'Dinheiro'),
    ('Cartao de Credito', 'Cartao de Credito'),
    ('Cartao de Debito', 'Cartao de Debito'),
)

ENUM_PAGAMENTO_RECEBIDO = (
    ('Recebido', 'Recebido'),
    ('Nao Recebido', 'Nao Recebido'),
)

# Classes

class Aluguel(models.Model):
    cliente = models.ForeignKey('Cliente', verbose_name='Cliente',
        help_text="Clique no botão + para adicionar um novo cliente ou selecione um da lista")
    tema = models.ForeignKey('Tema', verbose_name='Tema da Festa',
        help_text="Clique no botão + para adicionar um novo tema ou selecione um da lista")
    endereco = models.ForeignKey('Endereco', verbose_name='Endereço da Festa',
        help_text="Clique no botão + para adicionar um novo endereço ou selecione um da lista")
    pagamento = models.ForeignKey('Pagamento', verbose_name='Pagamento',
        help_text="Clique no botão + para adicionar um novo pagamento")
    data = models.DateField(default=datetime.now, blank=True, verbose_name='Data do Aluguel',
        help_text="Insira aqui a data da festa/do aluguel. Exemplo: 01/01/2001")
    hora_inicio = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Hora do Início')
    hora_termino = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Hora do Término')

    def __unicode__(self):
        return self.cliente.nome + " - " + self.tema.nome

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Aluguéis'

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor do Pagamento',
        help_text="Exemplo: 555,00")
    tipo_pagamento = models.CharField(max_length=20, choices=ENUM_TIPO_PAGAMENTO, verbose_name='Tipo do Pagamento')
    data_pagamento = models.DateField(default=datetime.now, blank=True, null=False, verbose_name='Data do Pagamento',
        help_text="Exemplo: 31/12/1999")
    recebido = models.CharField(max_length=20, choices=ENUM_PAGAMENTO_RECEBIDO, verbose_name='Pagamento Recebido')

    def __unicode__(self):
        return ("#" + str(self.id) + ": " + self.tipo_pagamento)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

class ItemTema(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Item')
    descricao = models.TextField(max_length=500, verbose_name='Descrição do Item')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Item de Tema'
        verbose_name_plural = 'Itens de Tema'

class Tema(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Tema')
    cor_toalha = models.CharField(max_length=10, choices=ENUM_COR, verbose_name='Cor da Toalha')
    item_tema = models.OneToOneField(ItemTema, verbose_name='Item do Tema',
        help_text="Clique no botão + para adicionar um novo item ou selecione um da lista")

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

class Endereco(models.Model):
    logradouro = models.CharField(max_length=300, verbose_name='Logradouro',
        help_text="Exemplo: Avenida Presidente Epitácio Pessoa")
    numero = models.PositiveSmallIntegerField(default=0, verbose_name='Número',
        help_text="Insira o número do imóvel. Deixe '0' caso o imóvel não possua número.")
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento',
        help_text="Exemplo: 'Próximo à Academia do Bambam BIRRR' ou 'Apartamento 502'")
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cep = models.CharField(max_length=9, verbose_name='CEP',
        help_text="Exemplo: 58000-000")
    estado = models.CharField(max_length=20, choices=ENUM_ESTADO, verbose_name='Estado')

    def __unicode__(self):
        return self.logradouro + ", " + self.cidade + ", " + self.estado

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.ForeignKey(Endereco, verbose_name='Endereço',
        help_text="Clique no botão + para adicionar um novo endereço ou selecione um da lista")
    telefone = models.CharField(max_length=15, verbose_name='Telefone',
        help_text="Exemplo: (12) 3456-7890")
    cpf = models.CharField(max_length=14, verbose_name='CPF',
        help_text="Exemplo: 123.456.789-01")
    email = models.EmailField(max_length=200, verbose_name='E-mail',
        help_text="Exemplo: nome@provedor.com")
    data_nascimento = models.DateField(null=False, blank=True, verbose_name='Data de Nascimento',
        help_text="Exemplo: 01/01/1991")
    sexo = models.CharField(max_length=10, choices=ENUM_SEXO, verbose_name='Sexo')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'