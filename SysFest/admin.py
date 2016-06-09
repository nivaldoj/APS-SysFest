# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.contrib import admin
from SysFest.models import *

# Register your models here.

"""
Renomeia o nome do painel administrador
"""

"""
class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('SysFest - Administração')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('SysFest - Administração')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('SysFest - Administração')

admin_site = MyAdminSite()
"""


"""
Configurações em cada seção do painel administrador
"""

class TelaInicial(admin.ModelAdmin):
	pass

class TabelaAdmin(admin.ModelAdmin):
	pass

class AdminAluguel(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum 
	fields = ('cliente', 'tema', 'endereco', 'pagamento',
		'data', 'hora_inicio', 'hora_termino')

	# Colunas que devem aparecer
	list_display = ('ID_do_Aluguel', 'Nome_do_Cliente', 'Endereco_da_Festa', 
		'Tema_da_Festa', 'Data_da_Festa')

	""" Obtem as colunas para exibir no list_display """
	def ID_do_Aluguel(self, obj):
		return obj.id

	def Nome_do_Cliente(self, obj):
		return obj.cliente.nome

	def Tema_da_Festa(self, obj):
		return obj.tema.nome

	def Data_da_Festa(self, obj):
		return obj.data

	def Endereco_da_Festa(self, obj):
		return ( str(obj.endereco.logradouro) + ", " + str(obj.endereco.numero) + " - " + str(obj.endereco.cidade) )

	# Filtros a serem exibidos na esquerda
	list_filter = ('data', 'hora_inicio', 'hora_termino')

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['tema__nome', 'cliente__nome', 'endereco__logradouro', 'data']

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

class AdminPagamento(admin.ModelAdmin):
	# Campos que devem ser exibidos como radio button
	radio_fields = {"tipo_pagamento": admin.VERTICAL, "recebido": admin.HORIZONTAL}

	# Campos a serem exibidos na criacao de algum
	fields = ('valor', 'tipo_pagamento', 'data_pagamento', 'recebido')

	# Colunas que devem aparecer
	list_display = ('ID_do_Pagamento', 'Tipo_do_Pagamento',
		'Data_do_Pagamento', 'Pagamento_Recebido')

	""" Obtem as colunas para exibir no list_display """
	def ID_do_Pagamento(self, obj):
		return obj.id

	def Tipo_do_Pagamento(self, obj):
		return obj.tipo_pagamento

	def Data_do_Pagamento(self, obj):
		return obj.data_pagamento

	def Pagamento_Recebido(self, obj):
		return obj.recebido

	# Filtros a serem exibidos na esquerda
	list_filter = ('data_pagamento', 'tipo_pagamento', 'recebido')

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['tipo_pagamento', 'data_pagamento', 'recebido']

class AdminEndereco(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum
	fields = ('logradouro', 'numero', 'complemento', 'cidade', 'bairro', 'cep', 'estado')
	
	# Colunas que devem aparecer
	list_display = ('Logradouro', 'Numero', 'Cidade', 'Bairro', 'CEP', 'Estado')
	
	""" Obtem as colunas para exibir no list_display """
	def Logradouro(self, obj):
		return obj.logradouro

	def Numero(self, obj):
		return obj.numero

	def Cidade(self, obj):
		return obj.cidade

	def Bairro(self, obj):
		return obj.bairro

	def CEP(self, obj):
		return obj.cep

	def Estado(self, obj):
		return obj.estado

	# Filtros a serem exibidos na esquerda
	list_filter = ('cidade', 'estado')

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['logradouro', 'numero', 'complemento', 'cidade', 'bairro', 'cep', 'estado']

class AdminItemTema(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum
	fields = ('nome', 'descricao')

	# Colunas que devem aparecer
	list_display = ('Nome_do_Item', 'Descricao_do_Item')

	""" Obtem as colunas para exibir no list_display """
	def Nome_do_Item(self, obj):
		return obj.nome

	def Descricao_do_Item(self, obj):
		return obj.descricao

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['nome', 'descricao']

class AdminTema(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum
	fields = ('nome', 'cor_toalha', 'item_tema')

	# Colunas que devem aparecer
	list_display = ('Nome_do_Tema', 'Cor_da_Toalha', 'Item_do_Tema')

	""" Obtem as colunas para exibir no list_display """
	def Nome_do_Tema(self, obj):
		return obj.nome

	def Cor_da_Toalha(self, obj):
		return obj.cor_toalha

	def Item_do_Tema(self, obj):
		return obj.item_tema

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

	# Filtros a serem exibidos na esquerda
	list_filter = ('cor_toalha', 'item_tema__nome')

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['nome', 'cor_toalha', 'item_tema']	

class AdminCliente(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum
	fields = ('nome', 'endereco', 'telefone', 'cpf', 'email', 'data_nascimento', 'sexo')

	# Colunas que devem aparecer
	list_display = ('Nome', 'Endereco', 'Telefone', 'CPF', 'Email', 'Data_de_Nascimento', 'Sexo')

	""" Obtem as colunas para exibir no list_display """
	def Nome(self, obj):
		return obj.nome

	def Endereco(self, obj):
		return ( str(obj.endereco.logradouro) + ", " + str(obj.endereco.numero) + " - " + str(obj.endereco.cidade) )

	def Telefone(self, obj):
		return obj.telefone

	def CPF(self, obj):
		return obj.cpf

	def Email(self, obj):
		return obj.email

	def Data_de_Nascimento(self, obj):
		return obj.data_nascimento

	def Sexo(self, obj):
		return obj.sexo

	# Filtros a serem exibidos na esquerda
	list_filter = ('endereco__estado', 'sexo')

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['nome', 'telefone', 'cpf', 'email', 'data_nascimento', 'sexo']

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True



""" 
Registra os modulos no Admin 
"""
admin.site.register(Aluguel, AdminAluguel)
admin.site.register(Pagamento, AdminPagamento)
admin.site.register(ItemTema, AdminItemTema)
admin.site.register(Endereco, AdminEndereco)
admin.site.register(Tema, AdminTema)
admin.site.register(Cliente, AdminCliente)


