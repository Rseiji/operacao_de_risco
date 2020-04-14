from project import db, login_manager
from project.models.usuario import Usuario
from flask_login import UserMixin



class Instrutor(Usuario, UserMixin):
    __tablename__ = 'instrutor'
    #breve = db.Column(db.String(5), nullable = False, unique = True)
    breve = db.Column(db.String(5), primary_key = True)
    voos = db.relationship('Voo', backref='instrutor', lazy=True)

    def get_id(self):
        return str(self.email)