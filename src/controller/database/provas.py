from controller.database.database import *
import psycopg2
import json

def consultaProvas():

  try:
    connection = DBconnect()

    cursor = connection.cursor()

    query = """SELECT * FROM provas"""

    cursor.execute(query)

    rows = cursor.fetchall()

    tableAttributes = ["id_prova", "materia"]

    data = TrataDados(rows,2,tableAttributes)

    return data
  
  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if connection is not None:
      connection.close()

def consulta_prova_especifica(id_prova):
  
  try:
    connection = DBconnect()

    cursor = connection.cursor()

    query = """SELECT id_prova FROM provas WHERE id_prova = '{id}'""".format(id = id_prova)

    cursor.execute(query)

    rows = cursor.fetchone()

    tableAttributes = ["id_prova", "materia"]

    data = TrataDados(rows,1,tableAttributes)

    return data
  
  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if connection is not None:
      connection.close()

def cadastraProva(materia):
  try:

    connection = DBconnect()

    cursor = connection.cursor()

    query = """INSERT INTO provas(materia) VALUES('{materia}')""".format(materia=materia)

    cursor.execute(query)

    connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError)as error:
    
    print(error)

  finally:
    if(connection is not None):
      connection.close()