import os
import ag.app

from flask import Blueprint, jsonify, render_template, current_app , request , session, redirect, url_for, send_from_directory

from donaclotilde.model import Model

from random import randint

asd = Model()

#bp para a logica de login e segurança

bp = Blueprint('users' , __name__ )


@bp.route('/login', methods = ['GET','POST'])
def login():			

	if request.method == 'POST':
		data = [request.form['email'] ,request.form['senha']]

		validator = asd.login(data)


		if validator:
			if validator[0][1] != 'True':
				return render_template('validar.html', date=data)
			
			session['username'] = validator[0]
			return redirect(url_for('tnp.painel'))
		else:
			return render_template('login.html' , login =True)
		
	return render_template('login.html' , login = False)
@bp.route("/arquivos", methods=["GET"])
def lista_arquivos():
	DIRETORIO="/"
	arquivos = []

	for nome_do_arquivo in os.listdir(DIRETORIO):
		endereco_do_arquivo = os.path.join(DIRETORIO, nome_do_arquivo)
		
		arquivos.append(nome_do_arquivo)

	#asd = send_from_directory(DIRETORIO,"style.css", as_attachment=True)

			
	return arquivos

@bp.route('/bbb', methods = ['GET'])
def baixa():			
	diretorio ='./donaclotilde/' 
	return send_from_directory(diretorio,"database.db", as_attachment=True)
	#return send_from_directory(diretorio,"style.css")
	#return diretorio


@bp.route('/validate',methods=['POST'])
def validate():
	
	data = asd.validar_email(request.form['email'], request.form['validar'])
	
	if data:
		
		asd.validar_email_confirmar(data[0][0])

		return redirect(url_for('tnp.painel'))

	
		
	return render_template('validar.html', data=data)





@bp.route('/create', methods = ['GET','POST'])
def create():			
	

	if request.method == 'POST':
		
		key = str(randint(10000, 99999))
		
		data = [
				request.form['nome'] ,
				request.form['email']+"@ceagesp.gov.br" ,
				request.form['seccao'] ,
				request.form['matricula'] ,
				request.form['senha'],
				key
				]
		
		validator = asd.criar_cadastro(data)
		#aqui mandar email para *request.form['email']+"@ceagesp.gov.br" 
		#com a varialvel key!!!

		if validator:
			return render_template('cadastrar.html',cadastro = True)
		else:
			return render_template('cadastrar.html' , login =True)
		
	return render_template('cadastrar.html',login = False)



#criar painel para mostrar dados de usuario, termos, pendencias
@bp.route('/show/<id>', methods = ['GET'])
def show(id = 0):			
	return 'show'+id




@bp.route('/')
def index():
	return redirect(url_for('users.login'))




def configure(app):
	app.register_blueprint(bp)

