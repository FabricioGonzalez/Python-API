from flask import Flask, request

@app.route("/", methods=["GET"])
def index():
  return {"Bem Vindo Usuário": "Digite olá mundo no fim da url"}

@app.route("/olamundo", methods=["GET"])

def olaMundo():
  return {"ola":"mundo"}

@app.route("/cadastro/alunos", methods=["POST"])
def cadastraAluno():
  body = request.get_json()
  print(body)
  return body