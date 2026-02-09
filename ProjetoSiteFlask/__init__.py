from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Configurações de Segurança e Persistência
# A SECRET_KEY garante a integridade dos formulários e proteção contra ataques CSRF
app.config['SECRET_KEY'] = 'cf5af0adf7da861043df694a55319216exit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'

# Inicialização das extensões do ecossistema Flask
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Definição das rotas de redirecionamento para controle de acesso (login_required)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Importação tardia das rotas e modelos para prevenir erros de importação cíclica (Circular Import)
from ProjetoSiteFlask import routes
from ProjetoSiteFlask import models