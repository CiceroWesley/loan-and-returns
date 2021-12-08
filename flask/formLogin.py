from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   usuario = StringField('Nome de Usuário', validators=[DataRequired()])
   senha = PasswordField('Senha: ', validators=[DataRequired()])
   enviar = SubmitField('Entrar')
