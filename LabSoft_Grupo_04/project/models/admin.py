from project.models.usuario import Usuario
from project import db
from flask_login import UserMixin

class Admin(Usuario, UserMixin):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)

    def get_id(self):
        return str(self.email)