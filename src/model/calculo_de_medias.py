def calculo_media_prova(lista_respostas_aluno,lista_respostas_gabarito):

  peso_total = 0
  nota = 0
  nota_final_prova = 0
  i = 0
  while(i<10):
    
    p = lista_respostas_gabarito[i][2]

    if(lista_respostas_aluno[i][0] == lista_respostas_gabarito[i][1]):

      peso_total+= p 
      print(peso_total)

      nota += (1*p)
      print(nota)

    elif(lista_respostas_aluno[i][0] != lista_respostas_gabarito[i][1]):
      peso_total = peso_total+p
      print(peso_total) 

      nota+= (0*p)
    i+=1
  
  nota_final_prova = (nota*10)/peso_total 

  return nota_final_prova

def calculo_media_final_aluno(lista_dados_notas):

  i = 0
  nota = 0
  while(i < len(lista_dados_notas)):
    
    nota+= lista_dados_notas[i][0]
    i+=1

  nota_final = nota/i
  
  return nota_final

