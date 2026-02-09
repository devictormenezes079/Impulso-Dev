import os
import secrets
from PIL import Image
from flask import render_template, redirect, url_for, flash, request
from ProjetoSiteFlask import app, database, bcrypt
from ProjetoSiteFlask.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from ProjetoSiteFlask.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
def home():
    """Rota da página inicial que lista todos os posts de forma dinâmica."""
    posts = Post.query.order_by(Post.data_criacao.desc()).all()
    return render_template('home.html', posts=posts)

def salvar_imagem(imagem):
    """
    Função auxiliar para tratar uploads:
    1. Gera um nome aleatório (hash) para evitar ficheiros duplicados.
    2. Redimensiona a imagem para 200px para poupar espaço no servidor (Pillow).
    """
    codigo = secrets.token_hex(8)
    _, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo) 
    return nome_arquivo

@app.route('/post/<int:post_id>/excluir', methods=['POST'])
@login_required
def excluir_post(post_id):
    """Lógica de segurança: Verifica se o utilizador atual é o autor antes de apagar o post."""
    post = Post.query.get_or_404(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluído com sucesso!', 'alert-success')
    return redirect(url_for('home'))