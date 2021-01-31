
def cadastra_questoes(questao,id_prova):

  query = """INSERT INTO questoes(pergunta,id_prova) VALUES ('{questao}',{id_prova})""".format(questao= questao, id_prova= id_prova)
  
  return query

def consulta_questoes(id_prova):

  query = """SELECT questoes.id_questao FROM provas INNER JOIN questoes ON provas.id_prova = questoes.id_prova WHERE questoes.id_prova = {id_prova}""".format(id_prova=id_prova)
  
  return query

def consulta_questoes_prova(id_prova):

  query = """SELECT questoes.id_questao, questoes.pergunta FROM provas INNER JOIN questoes ON provas.id_prova = questoes.id_prova WHERE questoes.id_prova = {id_prova}""".format(id_prova=id_prova)

  return query