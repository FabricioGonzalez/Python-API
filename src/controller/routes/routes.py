from controller.wrapper.wrapper import *
from controller.database.alunos import *
from flask import request,jsonify

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


