import psycopg2
import collections
import json

def DBconnect():

  try: 
    
    connection=psycopg2.connect(dbname='app', user="postgres", password="fabricio", host="localhost", port="4000")
    
  except: 
    print("Não foi possivel conectar")
  
  return connection

def CriaTabela():
  
  try:
    
    connection = DBconnect()

    cursor = connection.cursor()

    query1 = """CREATE TABLE alunos(
    id_aluno INTEGER NOT NULL,
    nome VARCHAR(30),
    PRIMARY KEY(id_aluno)
    )"""

    query2 = """CREATE TABLE provas(
    id_prova INTEGER NOT NULL,
    materia VARCHAR(30),
    id_pergunta INTEGER NOT NULL,
    PRIMARY KEY(id_prova),
    CONSTRAINT fk_id_pergunta FOREIGN KEY (id_pergunta) REFERENCES perguntas(id_pergunta)
    )"""

    query3 = """CREATE TABLE respostas(
      id_resposta INTEGER NOT NULL,
      
      id_aluno INTEGER NOT NULL,
      PRIMARY KEY(id_resposta),
      CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno)
    )
    """

    query4 = """CREATE TABLE perguntas(
      id_pergunta INTEGER NOT NULL,
      questao1 TEXT,
      questao2 TEXT,
      questao3 TEXT,
      questao4 TEXT,
      questao5 TEXT,
      questao6 TEXT,
      questao7 TEXT,
      questao8 TEXT,
      questao9 TEXT,
      questao10 TEXT,
      PRIMARY KEY(id_pergunta)
    )
    
    """
    query5 = """CREATE TABLE gabaritos(
      alternativa1 VARCHAR(5),
      alternativa2 VARCHAR(5),
      alternativa3 VARCHAR(5),
      alternativa4 VARCHAR(5),
      alternativa_certa VARCHAR(5),
      id_pergunta INTEGER,
      CONSTRAINT fk_id_pergunta FOREIGN KEY (id_pergunta) REFERENCES perguntas(id_pergunta)
    )
    """


    cursor.execute(query1)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    cursor.execute(query2)

    connection.commit()
  
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  
  finally:
    if connection is not None:
      connection.close()

CriaTabela()

def TrataDados(rows,r_length,tableNameArray):

    lista = []

    for row in rows:
     
      data = collections.OrderedDict()
      
      for x in row:
       
        y = 0
        
        while y < r_length:
          data[tableNameArray[y]] = row[y]
          y+=1

      lista.append(data)
    Json = json.dumps(lista)
    return Json
