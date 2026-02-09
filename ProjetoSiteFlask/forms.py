from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from ProjetoSiteFlask.models import Usuario

class FormCriarConta(FlaskForm):
    """Validação de registro: Garante integridade de e-mail e força de senha."""
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormEditarPerfil(FlaskForm):
    """Processamento de atualização cadastral e upload de mídia (fotos)."""
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    
    # Campos de competências mapeados como Booleanos para renderização em Checkboxes
    curso_python = BooleanField('Python Impressionador')
    curso_sql = BooleanField('SQL Impressionador')
    # ... outros campos mapeados aqui
    
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        """Lógica de validação customizada para evitar duplicidade de e-mails em atualizações."""
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Este e-mail já está sendo utilizado por outro usuário.')