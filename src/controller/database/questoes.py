from controller.database.database import *
from controller.database.provas import consulta_provas_especifica
import psycopg2
import json

def inserirQuestoes(questao,id_prova):

  try:
    
    connection = DBconnect()

    cursor = connection.cursor()

    prova = consulta_prova_especifica(id_prova)

    query = """INSERT INTO questoes(pergunta,id_prova) VALUES ('{questao}','{id_prova}')""".format(questao = questao, id_prova = id_prova)

    cursor.execute(query)

    connection.commit()

    cursor.close()

  except(Exception, psycopg2.DatabaseError) as error:
    print(error)
  
  finally:
    if(connection is not None):
      connection.close()


"""def consultaQuestoes(id_prova):"""
  
