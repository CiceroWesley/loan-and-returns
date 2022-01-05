from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class UsuarioForm(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
    username = StringField(u'Nome de usuário: ',validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
    email = EmailField('E-mail: ', validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
    senha = PasswordField('Senha: ',validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
    enviar = SubmitField('CADASTRAR')


