import psycopg2
import collections
import json

def db_connect():

  try: 
    
    connection=psycopg2.connect(dbname='app', user="postgres", password="fabricio", host="localhost", port="4000")
    
  except: 
    print("Não foi possivel conectar")
  
  return connection

def cria_tabelas():
  
  try:
    
    connection = db_connect()

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
    peso INTEGER,
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
    query8 = """Create table notas_finais(
    id_aluno INTEGER not null,
    nota float not null,
    CONSTRAINT fk_id_aluno FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
    );"""

    lista = [query1,query2,query3,query4,query5,query6,query7,query8]

    lista_de_tabelas = ["alunos","provas","questoes","alternativas","gabaritos","notas","respostas_alunos","notas_finais"]

    i = 0

    while(i < 8):
      
      query = """select exists(select * from information_schema.tables where table_name='{item}')""".format(item = lista_de_tabelas[i])

      cursor.execute(query)
      y = 0
      exists = bool(cursor.fetchone()[y])
      y+=1
      if(exists):

        print("""{item} já existe""".format(item = lista_de_tabelas[i]))
      
      else:

        print("""criando {item}""".format(item = lista_de_tabelas[i]))

        cursor.execute(lista[i])   

      i+=1
    connection.commit()
  
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  
  finally:
    if connection is not None:
      connection.close()

def trata_dados(rows,r_length,table_name_array):

    lista = []

    for row in rows:
      data = collections.OrderedDict()
      for x in row:
       
        y = 0
        while y < r_length: 
          data[table_name_array[y]] = row[y]
          
          y+=1

      lista.append(data)
    
    Json = json.dumps(lista)
    return Json

def insere_dados(query):
  
  try:

    connection = db_connect()

    cursor = connection.cursor()

    tipo = type(query)

    if(tipo == str):

      cursor.execute(query)

      connection.commit()
    
    elif(tipo == list):
      for item in query:
        cursor.execute(query)

        connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if(connection is not None):
      connection.close()

def consulta_dados(query):
  try: 
    
    connection = db_connect()

    cursor = connection.cursor()

    cursor.execute(query)

    dados = cursor.fetchall()

    return dados

  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if(connection is not None):
      connection.close()

def deleta_dados(query):
   
  try:
    connection = db_connect()

    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if(connection is not None):
      connection.close()

def atualiza_dados(query):
     
  try:
    connection = db_connect()

    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if(connection is not None):
      connection.close()