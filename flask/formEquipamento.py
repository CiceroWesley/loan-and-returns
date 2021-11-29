from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EquipamentoForm(FlaskForm):
    nome = StringField('Nome do equipamento', validators=[DataRequired()])
    enviar = SubmitField('CADASTRAR')