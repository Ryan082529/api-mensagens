from db import db
class Mensagens(db.Model):
    __tablename__='mensagens'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    conteudo= db.Column(db.String(255), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def to_dict(self):
        return {
            'id' : self.id,
            'conteudo': self. conteudo,
            'autor_id': self.autor_id  
        }
      

