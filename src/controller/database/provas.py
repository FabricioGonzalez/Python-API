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

    tableAttributes = ["id_prova", "id_materia", "id_pergunta"]

    data = TrataDados(rows,3,tableAttributes)

    return data
  
  except(Exception, psycopg2.DatabaseError)as error:
    print(error)

  finally:
    if connection is not None:
      connection.close()