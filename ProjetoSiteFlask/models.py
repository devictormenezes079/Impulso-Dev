from ProjetoSiteFlask import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader  
def load_usuario(id_usuario):
    """Callback do Flask-Login para recuperar a instância do usuário via Primary Key."""
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    """Entidade Usuário: Armazena credenciais e competências (serializadas em string)."""
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    cursos = database.Column(database.String, nullable=False, default='Não Informado')
    
    # Relacionamento One-to-Many: Um autor pode possuir múltiplas postagens
    posts = database.relationship('Post', backref='autor', lazy=True)

class Post(database.Model):
    """Entidade Post: Armazena postagens vinculadas a um autor via Chave Estrangeira."""
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    
    # FK vinculando o post ao ID único do usuário (Autor)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)