import psycopg2

def DBconnect():

  try: 
    
    connection=psycopg2.connect(dbname='app', user="postgres", password="fabricio", host="localhost", port="4000")
    
  except: 
    print("Não foi possivel conectar")
  
  return connection