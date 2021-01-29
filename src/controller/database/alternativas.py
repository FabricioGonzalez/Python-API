def cadastra_alternativas(alternativas,id_questao):
 
    for alternativa_atual in alternativas:

      query_list = []

      query = """INSERT INTO alternativas(alternativa, id_questao) 
      VALUES ('{alternativa}', {id_questao})
      """.format(id_questao = id_questao, alternativa = alternativa_atual)

      query_list.append(query)

      return query_list