
def cadastra_questoes(questao,id_prova):

  query = """INSERT INTO questoes(pergunta,id_prova) VALUES ('{questao}',{id_prova})""".format(questao= questao, id_prova= id_prova)
  
  return query

"""def consultaQuestoes(id_prova):"""
  
