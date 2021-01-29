from controller.wrapper.wrapper import *
from controller.database.index import *
from flask_cors import CORS

CORS(app)

@app.route("/",methods=['GET'])
def ola():
  return "Olá"

@app.route("/alunos",methods=['GET'])
def endpoint_consulta_aluno():

  query = consulta_aluno()

  data = consulta_dados(query)

  dados = trata_dados(data,2,["id_aluno","nome"])

  return jsonify(dados)

@app.route("/alunos/cadastro",methods=['POST'])
def endpoint_cadastra_aluno():
  
  body= request.get_json()

  query = cadastra_aluno(body["id"],body["nome"])

  insere_dados(query)

  return "{nome},\nCadastrada com sucesso".format(nome=body["nome"])

@app.route("/alunos/delete/<int:id>/",methods=['DELETE'])
def endpoint_deleta_aluno(id):
  
  query = deleta_aluno(id)

  deleta_dados(query)

  return "deletado"

@app.route("/alunos/delete/<string:nome>/",methods=['DELETE'])
def endpoint_deleta_aluno_por_nome(nome):
  
  query = deleta_aluno(nome)

  deleta_dados(query)

  return "deletado"

@app.route("/alunos/resposta/cadastro",methods=['POST'])
def endpoint_cadastra_respostas_de_alunos():

  body = request.get_json()
  
@app.route("/provas",methods=["GET"])
def endpoint_consulta_provas():
  
  query = consulta_provas()

  data = consulta_dados(query)

  dados = trata_dados(data,2,["id_prova","materia"])

  return jsonify(dados)
  
@app.route("/provas/cadastro",methods=["POST"])
def endpoint_cadastra_provas():

  body = request.get_json() 
  

  return jsonify(body)



