from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from project.models.voo import Voo


class AvaliaForm(FlaskForm):
    nota = IntegerField('Nota', validators=[DataRequired(), NumberRange(min=0, max=100, message=None)])
    voo_id = IntegerField('ID do Voo', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_voo(self, voo_id):
        user = Voo.query.filter_by(voo_id=voo_id.data).first()
        if not user:
            raise ValidationError('Voo não cadastrado.')
    

    
 