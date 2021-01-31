from controller.wrapper.wrapper import *
from controller.database.index import *
from model.calculo_de_medias import *
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
      
      while(y<11):
        
        q = questao["""questao{i}""".format(i=y)]

        pergunta = q["pergunta"]
      
        insere_dados(cadastra_questoes(pergunta,id_prova))
        y+=1          

      query_de_questoes = consulta_questoes(id_prova)
      
      lista = consulta_dados(query_de_questoes)

      c = 1
      while(c<=10):
       
        q = questao["""questao{n}""".format(n=c)]

        i = 1

        while(i < 5):

          query_de_alternativas = cadastra_alternativas(q["""alternativa{n}""".format(n=i)],lista[c-1][0])

          insere_dados(query_de_alternativas)    

          i+=1
        
        query_gabarito = cadastra_gabarito(id_prova,lista[c-1][0],q["alternativa_certa"],q["peso"])

        insere_dados(query_gabarito)

        c+=1  
  else: 
    
    questoes = body["questoes"]

    for questao in questoes:
      
      y=1
      
      while(y<11):
        
        q = questao["""questao{i}""".format(i=y)]

        pergunta = q["pergunta"]
      
        insere_dados(cadastra_questoes(pergunta,id_prova))

        y+=1          

      query_de_questoes = consulta_questoes(id_prova)
      
      lista = consulta_dados(query_de_questoes)

      print(lista)
      
      c = 1
      
      while(c<=10):
       
        q = questao["""questao{n}""".format(n=c)]

        i = 1

        while(i < 5):

          query_de_alternativas = cadastra_alternativas(q["""alternativa{n}""".format(n=i)],lista[c-1][0])

          insere_dados(query_de_alternativas)    

          i+=1
        
        query_gabarito = cadastra_gabarito(id_prova,lista[c-1][0],q["alternativa_certa"],q["peso"])

        insere_dados(query_gabarito)
        c+=1  

  return body, "Prova cadastrada com sucesso!!"

@app.route("/provas/aplicacao/<int:id_prova>",methods=["GET"])
def endpoint_aplicacao_de_prova(id_prova):
  
  query_prova = aplica_prova(id_prova)

  query_questoes = consulta_questoes_prova(id_prova)

  dados_questoes = consulta_dados(query_questoes)

  dados_prova = consulta_dados(query_prova)
  
  c = 0
  lista = []
  lista_resultado = []
  dados_prova = {"materia":dados_prova[0][0]}
  lista_resultado.append(dados_prova)

 
  while(c < 10):
   
    q = dados_questoes[c]

    query_de_alternativas = consulta_alternativas(q[0])
    
    dados_alternativa = consulta_dados(query_de_alternativas)

    diciot= {"alternativa1":dados_alternativa[0][0],"alternativa2":dados_alternativa[1][0],"alternativa3":dados_alternativa[2][0],"alternativa4":dados_alternativa[3][0]}
    lista_resultado.append([{"""pergunta{c}""".format(c=c+1):q[1]},diciot])
    c+=1
       
  response = jsonify(lista_resultado)

  return response

@app.route("/calculo/notas/aluno/<int:id_aluno>/provas/<int:id_prova>",methods=["GET"])
def endpoint_calculo_de_notas(id_aluno,id_prova):

  query = consulta_aluno(id_aluno)

  dados_aluno = consulta_dados(query)

  query_respostas_aluno = consulta_respostas_alunos(id_aluno,id_prova)

  query_respostas_prova = consulta_gabarito(id_prova)

  dados_respostas_aluno = consulta_dados(query_respostas_aluno)

  dados_respostas_prova = consulta_dados(query_respostas_prova)

  media_prova = calculo_media_prova(dados_respostas_aluno,dados_respostas_prova)

  print(media_prova)

  query_registro_de_nota_aluno = cadastra_notas(media_prova,id_aluno,id_prova)

  insere_dados(query_registro_de_nota_aluno)

  response = agente_de_respostas("""dados_aluno {dados}""".format(dados= dados_aluno))

  return response

@app.route("/consulta/notas/aluno/<int:id_aluno>",methods=["GET"])
def endpoint_consulta_notas_aluno(id_aluno):
  query_de_notas = consulta_notas(id_aluno)

  dados_notas = consulta_dados(query_de_notas)

  resultado = trata_dados(dados_notas,1,["nota"])

  response = agente_de_respostas(resultado)

  return response

@app.route("/consulta/notas/alunos/",methods=["GET"])
def endpoint_consulta_notas_alunos():

  query_de_notas = consulta_notas()

  dados_notas = consulta_dados(query_de_notas)

  resultado = trata_dados(dados_notas,3,["id_aluno","id_prova","nota"])

  response = agente_de_respostas(resultado)

  return response

@app.route("/calculo/notas_finais/aluno/<int:id_aluno>",methods=["GET"])
def endpoint_cadastra_nota_final(id_aluno):

  query_de_notas = consulta_notas(id_aluno)

  dados_notas = consulta_dados(query_de_notas)

  nota_final = calculo_media_final_aluno(dados_notas)

  insere_dados(cadastra_notas_finais(id_aluno,nota_final))

  response = agente_de_respostas("nota_final: {nota}".format(nota= nota_final))

  return response

@app.route("/consulta/notas_finais/alunos/",methods=["GET"])
def endpoint_consulta_notas_finais_alunos():
  query_de_notas = consulta_notas_finais()

  dados_notas = consulta_dados(query_de_notas)

  resultado = trata_dados(dados_notas,2,["id_aluno","nota"])

  response = agente_de_respostas(resultado)

  return response

@app.route("/consulta/notas_finais/aluno/<int:id_aluno>",methods=["GET"])
def endpoint_consulta_notas_finais_aluno(id_aluno):
  query_de_notas = consulta_notas_finais(id_aluno)

  dados_notas = consulta_dados(query_de_notas)

  resultado = trata_dados(dados_notas,2,["id_aluno","nota"])

  response = agente_de_respostas(resultado)

  return response