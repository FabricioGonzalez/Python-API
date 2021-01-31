
def consulta_aluno(*id_aluno):
  
  if(id_aluno):

    query = """SELECT * FROM alunos WHERE id_aluno = {id_aluno}""".format(id_aluno= id_aluno[0])
  
  else: 
    query = """SELECT * FROM alunos"""
  return query

def deleta_aluno(dado):
    
    tipo = type(dado)
    
    if(tipo == int):
      
      query = """DELETE FROM alunos 
      WHERE id_aluno = {data}""".format(data=dado)
      
      print("number")
      
      return query

    elif(tipo == str):
      
      query = """DELETE FROM alunos
      WHERE nome = '{data}'""".format(data=dado)

      print("string")

      return query

def cadastra_aluno(id,nome):

  query = """INSERT INTO alunos(id_aluno,nome)
  VALUES({id_aluno},'{nome_aluno}')""".format(id_aluno=id,nome_aluno=nome)

  return query
  
def cadastra_respostas_alunos(id_aluno,id_prova,alternativa):

  query = """INSERT INTO respostas_alunos(id_aluno,id_prova,alternativa) VALUES({id_aluno},{id_prova},'{alternativa}')""".format(id_aluno=id_aluno, id_prova=id_prova,alternativa=alternativa)

  return query

def consulta_respostas_alunos(id_aluno,id_prova):

  query = """SELECT respostas_alunos.alternativa FROM respostas_alunos INNER JOIN alunos ON respostas_alunos.id_aluno = alunos.id_aluno INNER JOIN provas ON provas.id_prova = respostas_alunos.id_prova WHERE alunos.id_aluno = {id_aluno} AND provas.id_prova = {id_prova}""".format(id_aluno=id_aluno,id_prova=id_prova)

  return query