> ## Python-API
  > 
  >API para cálculo de nota de alunos

  - ### EndPoints
    - #### ***GET alunos***


          Retorna todos os registros existentes de alunos no banco de dados.


        #### **URL:** 
        > http://localhost/alunos

        #### **Métodos HTTP:**
        > Metodos Aceitos:
        > 
        > - GET

        #### **Estrutura da Requisição**:
          A requisição feita a URL não requer corpo algum, apenas ser Feita como GET.
        
        #### **Informaçoes Adicionais:**

          Formato da Resposta: Json
                  
          Requer Autenticação: Não

        &nbsp;

        
    - #### ***POST alunos/cadastro***
          Cadastra um aluno no banco de dados.

        #### **URL:** 
        > http://localhost/alunos/cadastro
        
        #### **Métodos HTTP:**
        > Metodos Aceitos:
        > 
        > - POST


        #### **Estrutura da Requisição**:
          A requisição feita a URL deve ser um Objeto JSON contendo os parâmetros.
          O objeto JSON é enviado no corpo da requisição, e tratado pela API e enviado ao banco de dados.
        
        #### **Parâmetros:**

        &nbsp;

        | Nome | Obrigatório | Descrição | Tipo |
        | ------------- | :-----:| :--------:| :-------: |
        | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro***
        | nome | ***sim*** | Nome do aluno a ser registrado   | ***String*** |

        #### **Informaçoes Adicionais:**
          
          Formato da Resposta: Json
                  
          Requer Autenticação: Não




     

