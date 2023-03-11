import ag.app

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for

from donaclotilde.model import Model

asd = Model()

admin = Blueprint('admin' , __name__ , url_prefix='/admin')


@admin.route('/', methods = ['GET','POST'])
def index():			
		
	return "index<br>listar usuario, tnp, pendencias"





def configure(app):
	app.register_blueprint(admin)

