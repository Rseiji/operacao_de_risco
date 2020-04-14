from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, ValidationError
from project.models.instrutor import Instrutor
from project.models.aluno import Aluno
from project.models.usuario import Usuario

class DadosForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[('aluno', 'aluno'), ('instrutor', 'instrutor')], validators=[DataRequired()])
    cadastro = StringField('Cadastro', validators=[DataRequired()])
    submit = SubmitField('Aceitar')

    def validate_dados(self, cadastro, tipo):
        if (tipo.data == 'instrutor'):
            user = Instrutor.query.filter_by(breve=cadastro.data).first()
            if not user:
                raise ValidationError('Instrutor não cadastrado.')

        elif (tipo.data == 'aluno'):
            user = Aluno.query.filter_by(usuario_id=int(cadastro.data)).first()
            if not user:
                raise ValidationError('Aluno não cadastrado.')


