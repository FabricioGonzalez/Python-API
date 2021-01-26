from controller.database.database import *
import psycopg2
import json
import collections

def consultaAluno():
 
  try: 
    connection = DBconnect()

    cursor = connection.cursor()

    query = """SELECT * FROM alunos"""

    cursor.execute(query)

    rows = cursor.fetchall()

    lista = []
    for row in rows:
        data = collections.OrderedDict()
        data['id'] = row[0]
        data['nome'] = row[1]
        lista.append(data)

    Json = json.dumps(lista)

    cursor.close()

    return Json
  
  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  
  finally:
    if connection is not None:
      connection.close()


def deletaAluno(param):
  
  try:

    connection = DBconnect()

    cursor = connection.cursor()
    
    data = type(param)
    
    if(data == int):
      
      query = """DELETE FROM alunos 
      WHERE id_aluno = {data}""".format(data=param)

      cursor.execute(query)
      print("number")

    elif(data == str):
      
      query = """DELETE FROM alunos
      WHERE nome = '{data}'""".format(data=param)
      
      cursor.execute(query)
      print("string")

    connection.commit()

    cursor.close()
    print("ok")
  except(Exception, psycopg2.DatabaseError) as error:
      print(error) 

  finally:
    
    if connection is not None:
      connection.close()

def cadastraAluno(id,nome):
  
  try:
    connection = DBconnect()

    cursor = connection.cursor()

    query = """INSERT INTO alunos(id_aluno,nome)
    VALUES({id_aluno},'{nome_aluno}')""".format(id_aluno=id,nome_aluno=nome)

    cursor.execute(query)

    connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError)as error:
    print(error)
   
  finally:
    if connection is not None:
      connection.close