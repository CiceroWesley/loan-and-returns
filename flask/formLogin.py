from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   usuario = StringField('Nome de Usuário', validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
   senha = PasswordField('Senha: ', validators=[DataRequired()],render_kw={'class':'myclass','style':'width: 50%;'})
   enviar = SubmitField('Entrar')
