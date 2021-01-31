def cadastra_alternativas(alternativa,id_questao):

      query = """INSERT INTO alternativas(alternativa, id_questao) 
      VALUES ('{alternativa}', {id_questao})
      """.format(alternativa = alternativa,id_questao = id_questao)

      return query

def consulta_alternativas(id_questao):

      query = """SELECT alternativa, alternativas.id_questao FROM alternativas INNER JOIN questoes ON questoes.id_questao = alternativas.id_questao WHERE questoes.id_questao = {id_questao}""".format(id_questao=id_questao)
      return query