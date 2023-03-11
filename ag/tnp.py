import ag.app

from flask import Blueprint, render_template, request , session, redirect, url_for

from donaclotilde.model import Model

from datetime import date

asd = Model()

#blueprint reservado para as paginas do sistema
tnp = Blueprint('tnp' , __name__ , url_prefix='/tnp')


"""
trecho para ser descartado


#carrega a lista com busca
@tnp.route('/get_tnp/<busca>')
def get_tnp(busca):
	
	#retorna a lista da busca
	data = asd.ajax_list_tnp_filt(busca)
	#retorna os dados da paginação
	pag = asd.list_pag(busca)

	return render_template('tnp/ajax/ajax_tnp.html', data=data , pag=pag)


#carrega a lista com busca e limit
@tnp.route('/get_tnp/<limite>/<busca>')
def get_tnp_limit_filt(limite,busca):

	#retorna a lista da busca
	data = asd.ajax_list_tnp_filt(busca,limite)
	#retorna os dados da paginação
	pag = asd.list_pag(busca)
	pag[0].append(int(limite))

	return render_template('tnp/ajax/ajax_tnp.html', data=data , pag=pag)

#carrega a lista com busca e limit
@tnp.route('/get_tnp/<limite>/')
def get_tnp_limit_filtvazio(limite):

	#retorna a lista da busca
	busca = None
	data = asd.ajax_list_tnp_filt(busca ,limite)
	#retorna os dados da paginação
	pag = asd.list_pag(busca)
	pag[0].append(int(limite))

	return render_template('tnp/ajax/ajax_tnp.html', data=data , pag=pag)


#carrega a primeira lista
@tnp.route('/get_tnp/')
def get_tnp_limit():
	data = asd.ajax_list_tnp_filt_limit()
	#retorna os dados da paginação
	pag = asd.list_pag()
	return render_template('tnp/ajax/ajax_tnp.html', data=data , pag=pag)

"""

#carrega a pagina de lista mas não lista nada
@tnp.route('/list/')
def list_all():
	
	print('list/')
	if 'username' not in session:
		return redirect(url_for('users.login'))	
	
	data = asd.ajax_list_tnp_filt_limit()
	return render_template('tnp/tnp_listar.html',data=data)
	








@tnp.route('/get_empresas/<busca>')
def get_empresas(busca):
	data = asd.ajax_empresas(busca)
	return render_template('tnp/ajax/ajax_empresas.html',data=data)


@tnp.route('/get_local/<busca>')
def get_local(busca):
	data = asd.ajax_local(busca)
	
	return render_template('tnp/ajax/ajax_local.html',data=data)


#tem dois get_infração pois primeiro é caregado  vazio
@tnp.route('/get_infracao/<busca>')
def get_infracao(busca):
	
	data = asd.ajax_infracao(busca)
	
	return render_template('tnp/ajax/ajax_infracao.html',data=data)


@tnp.route('/get_infracao/')
def get_infracao_all():
	
	data = asd.ajax_infracao()
	
	return render_template('tnp/ajax/ajax_infracao.html',data=data)


@tnp.route('/ver/<id>')
def view(id):
	
	print('ver')
	if 'username' not in session:
		return redirect(url_for('users.login'))	

	data = asd.ver_tnp(id)
	infracao = asd.ver_infracao(data[0][3])

	return render_template('tnp_ver.html' , data=data, infracao=infracao)


@tnp.route('/add')
def add():
	print('add')
	data=date.today()
	data = data.strftime("%d/%m/%y")

	if 'username' not in session:
		return redirect(url_for('users.login'))	

	return render_template('tnp/tnp_incluir.html' , data_hoje=data)



@tnp.route('/insert_tnp', methods = ['POST'])
def insert_tnp():

	print('insert')

	if 'username' not in session:
		return redirect(url_for('users.login'))	
		
	
	empresa = request.form['input_busca_empresa']
	select_local = request.form['select_local']
	input_busca_infracao = request.form['input_busca_infracao']
	input_local_infracao = request.form['input_local_infracao']
	
	if input_local_infracao == "":
		input_local_infracao = select_local

	data = request.form['data']
	hora = request.form['hora']
	observacao = request.form['observacao']
	valor = "Pendente"
	status = "Pendente"
	datacria=date.today()

	criado = datacria.strftime("%d/%m/%y")
	termo = "Pendente"
	fiscal = session['username'][0]
	usuario = session['username'][0]

	dados = [empresa,
			select_local,
			input_busca_infracao,
			input_local_infracao,
			data,
			hora,
			observacao,
			valor,
			status,
			criado,
			termo,
			fiscal,
			usuario
			]


	colunas =['empresa_multa',
				'local_empresa_multa',
				'infracao_multa',
				'local_infracao_multa',
				'data_multa',
				'hora_multa',
				'observacao_multa',
				'valor_multa',
				'status_multa',
				'criado_em_multa',
				'termo_multa',
				'fiscal_multa',
				'usuario_multa'
				]

	asd.save_tnp(dados,colunas)

	return render_template('incluido.html')



@tnp.route('/create')
def create():
	print('create')
	
	if 'username' not in session:
		return redirect(url_for('users.login'))

	return render_template('incluir.html')






@tnp.route('/painel')
def painel():

	if 'username' not in session:
		return redirect(url_for('users.login'))
	return "tnp 3"
	#colocar funcoes de painel
	#numero de multas
	#mensagens de correção
	#avisos

@tnp.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('users.login'))

@tnp.route('/')
def index():
	if 'username' not in session:
		return redirect(url_for('users.login'))
	return redirect(url_for('tnp.painel'))




def configure(app):
	app.register_blueprint(tnp)

