> ## Python-API
  > 
  >API para cálculo de nota de alunos

  ### EndPoints
  - #### ***GET alunos***

        Retorna todos os registros existentes de alunos no banco de dados.

    #### **URL:** 
    > http://localhost/alunos

    #### **Métodos HTTP:**
    > Metodos Aceitos:
      > 
      > - ***GET***

    #### **Estrutura da Requisição**:
        A requisição feita a URL não requer corpo algum, apenas 
        ser Feita como GET.
    
    #### **Informaçoes Adicionais:**

        * Formato da Resposta: Json
                  
        * Requer Autenticação: Não

    &nbsp;


- #### ***POST alunos/cadastro***
      
        Cadastra um aluno no banco de dados.
        Após receber um código identificador do
        aluno e o seu nome.

    #### **URL:** 
    > http://localhost/alunos/cadastro
    
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***POST***


  #### **Estrutura da Requisição**:
        A requisição feita a URL deve ser um
        Objeto JSON contendo os parâmetros.
        O objeto JSON é enviado no corpo da requisição,
        e tratado pela API e enviado ao banco 
        de dados.
        
  #### **Parâmetros:**

    &nbsp;

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro***
    | nome | ***sim*** | Nome do aluno a ser registrado   | ***String*** |

    #### **Informaçoes Adicionais:**
      
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não


- #### DELETE **alunos/delete/<int:id>**
  
        Deleta um registro de aluno do banco de dados.
        De acordo com o identificador fornecido à URL. 
  
  - #### DELETE **alunos/delete/<string:nome>**
        
            Deleta um registro de 
            aluno do banco de dados.
            De acordo com o nome fornecido à URL. 

      #### **URL:**
      >http://localhost/alunos/delete/fernanda

  #### **URL:**
  > http://localhost/alunos/delete/1
  
    #### **Métodos HTTP:**
    > Métodos Aceitos
    >
    > - ***DELETE***

    #### **Estrutura da Requisição:**
        A requisição recebe em seu corpo um 
        Objeto JSON com o codigo identificador 
        do aluno, e consulta a base de
        dados para checar a existência, 
        caso haja um registro 
        condizente, o registro é deletado.

  #### **Parâmetros:**

  | Nome | Obrigatório | Descrição | Tipo |
  | ------------- | :-----:| :--------:| :-------: |
  | id_aluno | ***Sim*** | Código Identificado do aluno | ***Inteiro*** |
  | nome | ***Sim*** | Nome do aluno | ***String*** |

  #### **Informações Adicionais:**
  
        * Formato da Resposta: Json

        * Parâmetros Opcionais: id_aluno || nome
            
        * Requer Autenticação: Não

- #### **POST provas/cadastro/int:id>**

        Cadastra um novo registro de prova, recebendo 
        um código identificador da prova e uma matéria
        Ao cadastrar uma prova, cadastra-se também suas
        respectivas questões, alternativas, e o peso de
        cada uma de suas questões.
      
    #### **URL:**
    >http://localhost/provas/cadastro/1



  
