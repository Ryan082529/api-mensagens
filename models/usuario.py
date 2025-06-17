from db import db
class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email= db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    db.relationship('Mensagens', backref='usuarios', lazy=True)

def to_dict(self):
    return {
        'id' : self.id,
        'email': self. email,
        'nome': self. nome,  
        'senha': self. senha  
    }
