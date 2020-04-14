
# ======= Flask Imports ======= #

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import current_user

# ======= Project Imports ======= #

from project.models.usuario import Usuario
from project.models.aluno import Aluno
from project.models.instrutor import Instrutor

# ====== Forms code ======= #

class LoginForm(FlaskForm):
		email = StringField('Email', validators=[DataRequired()])
		senha = PasswordField('Senha', validators=[DataRequired()])
		submit = SubmitField('Login')
		def validate_user(self, email):
			user = Instrutor.query.filter_by(email=email.data).first()
			if not user:
				user = Aluno.query.filter_by(email=email.data).first()
				if not user:
					raise ValidationError('Instrutor não cadastrado.')
	