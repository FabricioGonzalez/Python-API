from controller.database.database import *
import psycopg2
import json

def inserirAlternativas(alternativas,id_questao):
    try:
    
      connection = DBconnect()

      cursor = connection.cursor()

      for alternativa_atual in alternativas:

        query = """INSERT INTO alternativas(alternativa, id_questao) VALUES ('{alternativa}', {id_questao})""".format(id_questao = id_questao, alternativa = alternativa_atual)

        cursor.execute(query)
        connection.commit()
      
      cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
      print(error)

    finally:
      if(connection is not None):
        connection.close()