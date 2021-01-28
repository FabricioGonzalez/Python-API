> ## Python-API
  > 
  >API para cálculo de nota de alunos

  - ### EndPoints
    - #### ***GET alunos***


          Retorna todos os registros existentes de alunos no banco de dados.


        #### **URL:** 
        > http://localhost/alunos


        #### **Informaçoes Adicionais:**

          
          Formato da Resposta: Json
                  
          Requer Autenticação: Não

        &nbsp;

        
    - #### ***POST alunos/cadastro***
          Cadastra um aluno no banco de dados.

        #### **URL:** 
        > http://localhost/alunos/cadastro
        
        #### **Informaçoes Adicionais:**
          
          Formato da Resposta: Json
                  
          Requer Autenticação: Não


        #### **Parametros:**

        &nbsp;

      | Nome | Obrigatório | Descrição | Tipo |
      | ------------- | :-----:| :--------:| :-------: |
      | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro***
      | nome | ***sim*** | Nome do aluno a ser registrado   | ***String*** |


     

