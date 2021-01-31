def cadastra_notas(notas,id_aluno,id_prova):
  
  query = """INSERT INTO notas(id_aluno,id_prova,nota) VALUES({id_aluno},{id_prova},{nota})""".format(nota=notas,id_aluno=id_aluno,id_prova=id_prova)

  return query

def cadastra_notas_finais(id_aluno,notas):
  
  query = """INSERT INTO notas_finais(id_aluno,nota) VALUES({id_aluno},{nota})""".format(id_aluno=id_aluno,nota=notas)

  return query

def consulta_notas_finais(*id_aluno):
  
  if(id_aluno):
    query = """SELECT * FROM notas_finais WHERE id_aluno = {id_aluno}""".format(id_aluno= id_aluno[0])

  else:
    query = """SELECT * FROM notas_finais"""

  return query


def consulta_notas(*id_aluno):
  
  if(id_aluno):
    
    query = """SELECT notas.nota FROM notas INNER JOIN alunos ON notas.id_aluno = alunos.id_aluno WHERE alunos.id_aluno = {id_aluno}""".format(id_aluno=id_aluno[0])

  else:
    
    query = """SELECT * FROM notas"""

  return query