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

    query1 = """Create table alunos(
    id_aluno INTEGER not null,
    nome varchar(50),
    primary key(id_aluno)
    );"""

    query2 = """Create table provas(
    id_prova SERIAL not null ,
    materia varchar(50),
    primary key(id_prova)
    );"""
    
    query3 = """Create table questoes(
    id_questao SERIAL not null,
    pergunta Text,
    id_prova INTEGER not null,
    primary key(id_questao),
    CONSTRAINT fk_id_prova FOREIGN KEY (id_prova) REFERENCES provas(id_prova)
    );"""

    query4 = """Create table alternativas(
    id_alternativa SERIAL not null,
    alternativa Text,
    id_questao INTEGER not null,
    primary key(id_alternativa),
    CONSTRAINT fk_id_questao FOREIGN KEY (id_questao) REFERENCES questoes(id_questao)
    );"""

    query5 = """Create table gabaritos(
    id_resposta_gabarito SERIAL not null,
    id_prova INTEGER not null,
    id_questao INTEGER not null,
    alternativa text,
    primary key(id_resposta_gabarito),
    CONSTRAINT fk_id_prova FOREIGN KEY (id_prova) REFERENCES provas(id_prova),
    CONSTRAINT fk_id_questao FOREIGN KEY (id_questao) REFERENCES questoes(id_questao)
    );"""

    query6 = """Create table notas(
    id_aluno INTEGER not null,
    id_prova INTEGER not null,
    nota float not null,
    CONSTRAINT fk_id_prova FOREIGN KEY (id_prova) REFERENCES provas(id_prova),
    CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
    );"""

    query7 = """Create table respostas_alunos(
    id_resposta_aluno SERIAL not null,
    id_prova INTEGER not null,
    id_aluno INTEGER not null,
    alternativa text,
    primary key(id_resposta_aluno),
    CONSTRAINT fk_id_prova FOREIGN KEY (id_prova) REFERENCES provas(id_prova),
    CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
    );"""

    lista = [query1,query2,query3,query4,query5,query6,query7]

    for item in lista:

      query = """SELECT EXISTS(SELECT FROM public
      WHERE table_name = '{item}')""".format(item = item)

      cursor.execute(query)
      y = 0

      exists = bool(cursor.fetchone()[y])

      y+=1

      if(exists):

        print("Já existe")
      
      else:

        cursor.execute(item)          

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
