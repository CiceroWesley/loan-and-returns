from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class EmprestimoForm(FlaskForm):
  equipamento = SelectField('Equipamento',coerce=int, render_kw={'class':'myclass','style':'width: 50%;'})
  enviar = SubmitField('Cadastrar')
