#!/usr/bin/python
# -*- coding: latin-1 -*-

#model usado como exemplo, suas consultas devem ser construidas conforme sua necessidade


from donaclotilde.donaclotilde import Donaclotilde

from datetime import date



from flask import g

import sqlite3


class Model(Donaclotilde):
	"""ATRIBUTOS DO Model HERDADOS DE Donaclotilde"""
	""" /entrada_select /entrada_count /entrada_from_table /entrada_where /entrada_insert /query """
	def __init__(self):
		super().__init__()
		pass

	def save(self,kwargs):
		#original
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		sql = self.set("user",values,columns)
		#print(sql)
		self.insert(sql)

	def update(self,kwargs):
		#original
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		self.where( 5 ,"id","=")
		
		sql = self.setup("user",values,columns)
		#print(sql)
		self.insert(sql)

	def list_all(self):
		#modificado
		self.select('*')
		
		self.from_table("dados")
		
		sql = self.get()
		data = self.result_list(sql)
		return data
	
	def list_tnp_limit_filt(self, limite = 0  , busca = None):
		#modificado
		
		self.select('termo_multa') 
		self.select('empresa_multa')
		self.select('data_multa')
		self.select('infracao_multa')
		self.select('valor_multa')
		self.select('id')

		
		self.from_table("cadastro_multa")
		
		if busca:
			self.where(busca,"empresa_multa")

		self.limit(limite,10)
		self.order_desc('id') 


		sql = self.get()
		data = self.result_list(sql)
		return data
	def save_tnp(self,dados,colunas):

		#modificado

		values=[x for x in dados]

		columns = [x for x in colunas]

		sql = self.set("cadastro_multa",values,columns)
		#print(sql)
		self.insert(sql)

	def ajax_empresas(self, busca = None):
		#modificado
		
		self.select('nome_permissionario') 
		
		self.from_table("empresas_area")
		
		if busca:
			self.where(busca,"nome_permissionario")

		sql = self.get()
		
		
		data = self.result_list(sql +" GROUP BY nome_permissionario")
		return data
	
	def ajax_local(self, busca = None):


		self.select('pavilhao') 
		self.select('area_banca') 

		self.from_table("empresas_area")
		
		if busca:
			self.where(busca,"nome_permissionario", "=")

		self.order_desc('pavilhao')

		sql = self.get()
		data = self.result_list(sql)
		
		return data

	def ajax_infracao(self, busca = None):


		self.select('codigo_infracao') 
		self.select('descricao_infracao') 

		self.from_table("infracao")
		
		if busca:
			self.where(busca,"descricao_infracao")

		#self.order_desc('codigo_infracao')

		sql = self.get()
		data = self.result_list(sql)
		
		return data


	def ajax_list_tnp_filt_limit(self, busca = None , indice=0):
		#modificado
		
		self.select('termo_multa') 
		self.select('empresa_multa')
		self.select('data_multa')
		self.select('infracao_multa')
		self.select('valor_multa')
		self.select('id')

		
		self.from_table("cadastro_multa")
		
		if busca:
			self.where(busca,"empresa_multa")
		
		self.limit(indice,10)
		
		self.order_desc('id') 

		sql = self.get()
		data = self.result_list(sql)
		return data

	def ajax_list_tnp_filt(self, busca = None , indice=0):
		#modificado
		
		self.select('termo_multa') 
		self.select('empresa_multa')
		self.select('data_multa')
		self.select('infracao_multa')
		self.select('valor_multa')
		self.select('id')

		
		self.from_table("cadastro_multa")
		
		if busca:
			self.where(busca,"empresa_multa")
		
		self.limit(indice,10)
		
		self.order_desc('id') 

		sql = self.get()
		data = self.result_list(sql)
		return data

	def list_pag(self, busca = None):
		#modificado
		self.count('termo_multa')
		self.from_table("cadastro_multa")
		
		if busca:
			self.where(busca,"empresa_multa")

		sql = self.get()
		data = self.result_list(sql)
		return data
	

	def ver_tnp(self,id):

		self.select('termo_multa') #0
		self.select('empresa_multa') #1
		self.select('local_empresa_multa') #2 
		self.select('infracao_multa') #3
		self.select('data_multa') #4
		self.select('hora_multa') #5
		self.select('local_infracao_multa') #6
		self.select('observacao_multa') #7
		self.select('fiscal_multa') #8
		
		self.select('*')

		
		self.from_table("cadastro_multa")

		self.where(id,"id","=")

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
	def ver_infracao(self,infracao):
		self.select('descricao_infracao')

		self.from_table("infracao")

		self.where(infracao,"codigo_infracao","=")

		sql = self.get()
		data = self.result_list(sql)
		return data

	def list_filter(self,search=None, coluna=None):
		
		#self.select('id')
		self.select('name')

		if coluna:
			self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			self.where_combining("AND")
			self.where("Josef Stalin","name","=")

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_filter_where(self,search=None, id=1):
		
		#self.select('id')
		self.select('name')
		self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name","LIKE","start")
			self.where_combining("AND")
			self.where_combining("(")

			self.where( id ,"id","=")
			self.where_combining("OR")
			self.where( "321" ,"password","=")

			self.where_combining(")")


		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_count(self, search):
		
		self.count('*')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			
			self.where_combining("OR")
			self.where("sta","name")
			
		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
		


	def list_limite(self):

		self.select('*')
		
		self.from_table("user")
		self.limit(3,2)
		sql = self.get()
		data = self.result_list(sql)
		return data

	def list_order(self):

		self.select('*')
		
		self.from_table("user")
		
		#self.order("name")
		#self.order_desc("name")
		
		self.order_desc("number")
		self.order_asc('name')
		
		sql = self.get()
		data = self.result_list(sql)
		return data


	def login(self,data):
		self.select('nome_users')
		self.select('verificado_users')

		self.from_table('users')

		self.where( data[0] ,"email_users","=")
		
		self.where_combining("AND")
		
		self.where( data[1] ,"senha_users","=")		

		sql = self.get()
		data = self.result_list(sql)
		
		if data != []:
			return data

		return False

	def validar_email(self, email, chave):

		self.select('id')

		self.from_table('users')

		self.where( email ,"email_users","=")
		
		self.where_combining("AND")
		
		self.where( chave ,"verificado_users","=")		

		sql = self.get()
		data = self.result_list(sql)
		
		if data != []:

			return data

		return False

	def validar_email_confirmar(self, id):

		values=["True"]
		columns=['verificado_users']
		
		self.where( id ,"id","=")
		
		sql = self.setup("users",values,columns)
		#print(sql)
		self.insert(sql)



	def criar_cadastro(self,data):
		#modificado

		columns=['nome_users','email_users','secao_users','matricula_users','senha_users','verificado_users','data']
		hoje = date.today()
		data.append(str(hoje))


		sql = self.set("users",data,columns)
		#print(sql)
		self.insert(sql)
		return True