from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from project.models.aluno import Aluno
from project.models.instrutor import Instrutor
from project.models.voo import Voo


class VooForm(FlaskForm):
    horaSaida = StringField('Saída "hh:mm"', validators=[DataRequired()])
    duracaoVoo = StringField('Duração "hh:mm"', validators=[DataRequired()])
    parecer = SelectField('Parecer', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[DataRequired()])
    aluno = StringField('Aluno', validators=[DataRequired(), Length(max=60)])
    instrutor = StringField('Instrutor', validators=[DataRequired(), Length(max=60)])
    submit = SubmitField('Cadastrar')

    def validate_instrutor(self, instrutor):
        user = Instrutor.query.filter_by(nome=instrutor.data).first()
        if not user:
            raise ValidationError('Instrutor não cadastrado.')
    
    def validate_aluno(self, aluno):
        user = Aluno.query.filter_by(nome=aluno.data).first()
        if not user:
            raise ValidationError('Aluno não cadastrado.')
