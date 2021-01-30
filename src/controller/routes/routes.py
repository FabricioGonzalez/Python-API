from controller.wrapper.wrapper import *
from controller.database.index import *
from flask_cors import CORS
import json

CORS(app)

@app.route("/",methods=['GET'])
def ola():
  return "Olá"

@app.route("/alunos",methods=['GET'])
def endpoint_consulta_aluno():

  query = consulta_aluno()

  data = consulta_dados(query)

  dados = trata_dados(data,2,["id_aluno","nome"])

  response =  agente_de_respostas(dados)

  return response

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

@app.route("/alunos/respostas/cadastro",methods=['POST'])
def endpoint_cadastra_respostas_de_alunos():

  body = request.get_json()
  
  respostas = body["respostas"]
  
  for alternativa in respostas:
    
    y=1
    
    while(y<=10):
      
      print(alternativa["""resposta{i}""".format(i=y)])
      
      insere_dados(cadastra_respostas_alunos(body["id_aluno"],body["id_prova"],alternativa["""resposta{i}""".format(i=y)]))
      
      y+=1

  return body

  
@app.route("/provas",methods=["GET"])
def endpoint_consulta_provas():
  
  query = consulta_provas()

  data = consulta_dados(query)

  dados = trata_dados(data,2,["id_prova","materia"])

  response =  agente_de_respostas(dados)

  return response
  
@app.route("/provas/cadastro/<int:id_prova>",methods=["POST"])
def endpoint_cadastra_provas(id_prova):

  body = request.get_json()

  query2 = consulta_prova_especifica(id_prova)

  data = bool(consulta_dados(query2))

  if(data != True):
          
    query = cadastra_prova(id_prova,body["materia"])

    insere_dados(query)

    y=1

    questoes = body["questoes"]

    for questao in questoes:
      
      y=1
      
      while(y<=10):
        
        q = questao["""questao{i}""".format(i=y)]

        pergunta = q["pergunta"]
        
        print(pergunta)

        insere_dados(cadastra_questoes(pergunta,id_prova))
        
        y+=1

  else: 

    y=1

    questoes = body["questoes"]

    for questao in questoes:
      
      y=1
      
      while(y<=10):
        
        q = questao["""questao{i}""".format(i=y)]

        pergunta = q["pergunta"]
        
        print(pergunta)

        insere_dados(cadastra_questoes(pergunta,id_prova))
        
        y+=1
      

  return body




