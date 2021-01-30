
def consulta_provas():

  query = """SELECT * FROM provas"""

  return query
  
def consulta_prova_especifica(id_prova):
  
  query = """SELECT id_prova FROM provas WHERE id_prova = {id}""".format(id = id_prova)
  
  return query

def cadastra_prova(id_prova, materia):

  query = """INSERT INTO provas(id_prova, materia) VALUES({id_prova}, '{materia}')""".format(id_prova= id_prova, materia=materia)

  return query