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

@app.route('/criar/<string:classe>', methods=['post'])
def criar(classe):
  resposta = jsonify({"status": "201", "result": "ok", "details": "Objeto criado!"})
  dados = request.get_json()
  try:
    if classe == "sala":
      novo = Sala(**dados)

    elif classe == "pessoa":
      numero_salas = Sala.query.count()
      numero_cafes = Cafe.query.count()
      if numero_salas != 0 or numero_cafes != 0:
        db_salas = db.session.query(Sala).all()
        db_cafes = db.session.query(Cafe).all()
        novo = Pessoa(**dados, sala = db_salas[0], cafe = db_cafes[0])
      else:
        resposta = jsonify({"status": "400", "result": "error", "details ": str(e)})


    elif classe == "cafe":
      numero_cafes = Cafe.query.count()
      if numero_cafes <= 1:
          novo = Cafe(**dados)
      else:
          resposta = jsonify({"status": "400", "result": "error", "details ": str(e)})
    
    db.session.add(novo)
    db.session.commit()
  except Exception as e:
    resposta = jsonify({"status": "400", "result": "error", "details ": str(e)})
  resposta.headers.add("Access-Control-Allow-Origin", "*")
  return resposta 


if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)