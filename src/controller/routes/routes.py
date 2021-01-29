from controller.wrapper.wrapper import *
from controller.database.alunos import *
from controller.database.provas import * 
from flask_cors import CORS

CORS(app)

@app.route("/",methods=['GET'])
def ola():
  return "Olá"

@app.route("/alunos",methods=['GET'])
def consulta_aluno():

  data = consultaAluno()

  return data

@app.route("/alunos/cadastro",methods=['POST'])
def cadastra_aluno():
  
  body= request.get_json()

  cadastraAluno(body["id"],body["nome"])

  return "{nome},\nCadastrada com sucesso".format(nome=body["nome"])

@app.route("/alunos/delete/<int:id>/",methods=['DELETE'])
def deleta_aluno(id):
  deletaAluno(id)
  return "deletado"

@app.route("/alunos/delete/<string:nome>/",methods=['DELETE'])
def deleta_aluno_por_nome(nome):
  deletaAluno(nome)
  return "deletado"

@app.route("/alunos/resposta/cadastro",methods=['POST'])
def cadastra_respostas_de_alunos():

  body = requests.get_json()
  


@app.route("/provas",methods=["GET"])
def consulta_provas():
  
  data = consultaProvas()

  return data
  
@app.route("/provas/cadastro",methods=["POST"])
def cadastra_provas():

  body = request.get_json() 
  

  return jsonify(body)



