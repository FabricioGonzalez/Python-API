
def consulta_aluno():
 
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
  