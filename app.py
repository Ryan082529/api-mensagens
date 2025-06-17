from flask import Flask, request, jsonify
from db import db
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db.init_app(app)
migrate = Migrate(app,db)

with app.app_context():
    from models.mensagens import Mensagens
    from models.usuario import Usuario
    db.create_all()




@app.route("/mensagens", methods=['post'])
def criar_mensagem():
    data = request.get_json()
    conteudo = data['conteudo']
    novaMensagem = Mensagens(conteudo=conteudo, autor_id=1)
    db.session.add(novaMensagem)
    db.session.commit()
    return jsonify({'msg': "mensagem criada com sucesso"}), 201



@app.route("/mensagens")
def listar_mensagens():
    mensagens = Mensagens.query.all()
    mensagens = [mensagem.to_dict() for mensagem in mensagens]
    return jsonify({'mensagens': mensagens}), 200
@app.route("/mensagens/<id>")
def obter_mensagem(id):
    mensagem = Mensagens.query.filter_by(id=id)
    if mensagem is not None: 
        return jsonify({"mensagem": mensagem.to_dict()}) 
    return jsonify({"msg": "mensagem não encontrada"})

@app.route("/mensagens/<id>", methods=['put'])
def atualizar_mensagem(id):
    data = request.get_json()
    conteudo = data['conteudo']
    mensagem = Mensagens.query.filter_by(id=id)
    if mensagem is None:
        return jsonify({'error': " mensagem não existente"})
    mensagem.conteudo = conteudo    
    return jsonify({"msg": "mensagem natualizada com sucesso"}), 200

@app.route("/mensagens/<id>", methods=['delete'])
def deletar_mensagem(id):
    mensagem = Mensagens.query.filter_by(id=id)
    if mensagem is None : 
        return jsonify({'error': " mensagem não existente"})
    db.session.delete(mensagem)
    db.session.commit()
    return jsonify({"mensagem": "Removida com sucesso"}),200

    