'''
Esse ambiente é apenas de testes!
 - Todo comando que se executa dentro do BD tem que está na estrutura:
    with app.app_context(): 
'''

from main import app, database
from ProjetoSiteFlask.models import Usuario, Post

# with app.app_context(): 
#     database.create_all()

# with app.app_context(): 
#     # Criando a variavel de usuário
#     usuario = Usuario(username="Victor", email="victor@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Joana", email="joana@gmail.com", senha="123457")

#     # Para adicionar os usuários é necessário dar um session e um commit.
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()
#----------------------------------------------------------------------------

#Buscar no BD:
# with app.app_context(): 
#     meus_usuarios = Usuario.query.all()
#     primeiro_usuario = Usuario.query.first()
#     print(meus_usuarios)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.posts)

# Busca a partir de uma condição
# Buscando um usuario que o id é = a 2
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste)
#     print(usuario_teste.email)

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(email='victor@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)
#----------------------------------------------------------------------------

# Buscando posts específicos
# Criando um post
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro Post Feito', corpo="Victor está aprendendo")
#     database.session.add(meu_post)
#     database.session.commit()

with app.app_context():
    post = Post.query.first()
    print(post.titulo)
    print(post.autor.email)
    print(post.id_usuario)