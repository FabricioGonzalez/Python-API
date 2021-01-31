def cadastra_gabarito(id_prova,id_questao,alternativa_certa,peso):

  query = """INSERT INTO gabaritos(id_prova,id_questao,alternativa,peso) VALUES({id_prova},{id_questao},'{alternativa}',{peso})""".format(alternativa=alternativa_certa,id_prova=id_prova,id_questao=id_questao,peso=peso)

  return query

def consulta_gabarito(id_prova):

  
  query = """SELECT gabaritos.id_questao, gabaritos.alternativa, gabaritos.peso FROM gabaritos INNER JOIN provas ON gabaritos.id_prova = provas.id_prova WHERE provas.id_prova = {id_prova}""".format(id_prova=id_prova)

  return query