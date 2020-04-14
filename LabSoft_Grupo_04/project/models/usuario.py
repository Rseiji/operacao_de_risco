from project import db

class Usuario(db.Model):
    __abstract__ = True
    #usuario_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False, unique = True)
    cpf = db.Column(db.String(11), nullable=False, unique = True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Usuario(Nome:'{self.nome}', email:'{self.email}'')"
