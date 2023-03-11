import ag.users
import ag.tnp
import ag.admin

from flask import Flask

users = ag.users
tnp = ag.tnp
admin = ag.admin

def create_app():

    app = Flask(__name__)
    app.config['TITLE'] = "Groselha Gigante"

    app.secret_key = b'guerra aos senhores'
    users.configure(app)
    tnp.configure(app)
    admin.configure(app)
    return app

application = create_app()
