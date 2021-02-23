from config import *
from models import Pessoa, Sala, Cafe

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "sala":
      dados = db.session.query(Sala).all()
    elif classe == "pessoa":
      dados = db.session.query(Pessoa).all()
    elif classe == "cafe":
      dados = db.session.query(Cafe).all()

    lista_jsons = [ x.json() for x in dados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)