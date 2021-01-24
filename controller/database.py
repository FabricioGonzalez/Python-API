import psycopg2

def DBconnect():

  try: 
    
    connection=psycopg2.connect(dbname='app', user="postgres", password="fabricio", host="localhost", port="4000")
    
    cursor = connection.cursor()
  
    query = """CREATE TABLE alunos(id_aluno INTEGER NOT NULL PRIMARY KEY,
    nome VARCHAR NOT NULL
    )"""
    cursor.execute(query)

    connection.commit()

    """ rows = cursor.fetchall()
    print("\n Rows: \n")
    for row in rows:
      print(" ",row[1])
  """
  except: 
    print("Não foi possivel conectar")