
def consulta_provas():

  query = """SELECT * FROM provas"""

  return query
  
def consulta_prova_especifica(id_prova):

  query = """SELECT id_prova FROM provas WHERE id_prova = {id}""".format(id = id_prova)
  
  return query

def cadastra_prova(id_prova, materia):

  query = """INSERT INTO provas(id_prova, materia) VALUES({id_prova}, '{materia}')""".format(id_prova= id_prova, materia=materia)

  return query

def aplica_prova(id_prova):
  
  #query = """SELECT provas.materia,questoes.pergunta,alternativas.alternativa FROM provas INNER JOIN questoes ON provas.id_prova = questoes.id_prova INNER JOIN alternativas ON alternativas.id_questao = questoes.id_questao WHERE questoes.id_prova = {id_prova}""".format(id_prova= id_prova)
  query = """SELECT materia FROM provas WHERE id_prova = {id_prova}""".format(id_prova= id_prova)              
  return query