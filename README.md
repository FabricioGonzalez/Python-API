> ## Python-API
  > 
  >API para cálculo de nota de alunos

## Como compilar:
  - Dê um Git clone.
  
  - Abra a pasta do projeto.

  - Ative o ambiente virtual env usando o comando (no Windows: env\Scripts\activate.bat),
  (no Linux ou MacOS: source tenv/bin/activate).

  - Rode o arquivo app.py na pasta src do projeto com o interpretador python.

  - Aí é só testar e ser feliz.

    ***O projeto roda com postgres, configurado para ouvir a porta 4000 do localhost e o banco de dados ouvido pela aplicação se chama "app".***

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

  #### **Estrutura da Requisição:**
        A requisição feita a URL deve ser um
        Objeto JSON contendo os parâmetros.
        O objeto JSON é enviado no corpo da requisição,
        e tratado pela API e enviado ao banco 
        de dados.

  #### **Exemplo do corpo da requisição:**
    ``{
    "id":"2",
    "nome":"Ana Belle"
    }``

  #### **Parâmetros:**

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro***
    | nome | ***sim*** | Nome do aluno a ser registrado   | ***String*** |
    
    &nbsp;
    
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
        A requisição recebe em sua URÇ codigo identificador 
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

- #### **POST provas/cadastro/int:id:prova>**

        Cadastra um novo registro de prova, recebendo 
        um código identificador da prova e uma matéria
        Ao cadastrar uma prova, cadastra-se também suas
        respectivas questões, alternativas, a alternativa correta da questão e o peso de
        cada uma de suas questões.

    #### **URL Exemplo:**
    >http://localhost/provas/cadastro/1
    
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***POST***

  #### **Estrutura da Requisição**:
        A requisição feita a URL deve receber um
        identificador da prova em sua URL via QueryString
        E um Objeto JSON para que possa tratado pela 
        API e enviado ao banco de dados.

  #### **Exemplo extrutura do corpo da requisição:**
    ``{
      "materia": "Lingua Portuguesa",
      "questoes": [
        {
        "questao1": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa":"todas as alternativas",
          "peso": 1
        },
        "questao2": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa":"todas as alternativas",
          "peso": 1
        },
        "questao3": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa":"todas as alternativas",
          "peso": 1
        },
        "questao4": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "todas as alternativas",
          "peso": 1
        },
        "questao5": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa":"todas as alternativas",
          "peso": 1
        },
        "questao6": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "todas as alternativas",
          "peso": 1
        },
        "questao7": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "todas as alternativas",
          "peso": 1
        },
        "questao8": {
          "pergunta": "Que o subtantivo relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "todas as alternativas",
          "peso": 1
        },
        "questao9": {
          "pergunta": "Que o p relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "todas as alternativas",
          "peso": 1
        },
        "questao10": {
          "pergunta": "Que o dado relacionado a casa",
          "alternativa1": "todas as alternativas",
          "alternativa2": "janela",
          "alternativa3": "tijolo",
          "alternativa4": "dado",
          "alternativa_certa": "dado",
          "peso": 1
        }
      }
    ]
  }``
        
  #### **Parâmetros:**

    &nbsp;

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | Matéria| ***sim*** | Matéria da prova | ***String***
    | Questôes | ***sim*** | Questões a serem cadastradas   | ***String*** |
    | Alternativas | ***sim*** | Alternativas a serem cadastradas | ***String*** |
    | Alternativa_certa | ***sim*** | Alternativa correta da questão | ***String***|
    | Peso | ***sim*** | O peso de cada questão para a determinação da nota final da prova | ***Inteiro***|

  #### **Informaçoes Adicionais:**

        * Formato da Resposta: Json
            
        * Requer Autenticação: Não



- #### **POST /alunos/respostas/cadastro**
        Cadastra as Respostas de um aluno
        para uma prova no banco de dados.
    #### **URL:** 
    > http://localhost/alunos/respostas/cadastro
    
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***POST***


    #### **Estrutura da Requisição:**
          A requisição feita a URL deve ser um
          Objeto JSON contendo os parâmetros.
          O objeto JSON é enviado no corpo da requisição,
          e tratado pela API e enviado ao banco 
          de dados.

    #### **Exemplo do corpo da Requisição:**
    ``{
        "id_aluno": 2,
        "id_prova": 1,
        "respostas": [
          {
            "resposta1": 	"todas as alternativas",
            "resposta2":	"todas as alternativas",
            "resposta3":"todas as alternativas",
            "resposta4": "todas as alternativas",
            "resposta5": "qualquer coisa",
            "resposta6": "todas as alternativas",	
            "resposta7": "outro",	
            "resposta8": "todas as alternativas",
            "resposta9": "n sei",
            "resposta10":	"dado"
          }
        ]
      }``
          
    #### **Parâmetros:**

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro***
    | id_prova | ***sim*** | Identificador da prova no banco de dados   | ***Inteiro*** |
    | Respostas | ***Sim*** | Respostas a serem cadastradas no banco de dados | ***String*** | 
    
    &nbsp;
    
    #### **Informaçoes Adicionais:**
        * Formato da Resposta: Json
            
        * Requer Autenticação: Não

- #### **GET /provas**
        Retorna todas as provas cadastradas
        no banco de dados.
    #### **URL:** 
    > http://localhost/provas
    
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição**:
        A requisição feita a URL não necessita
        de parâmetros.
        
    #### **Informaçoes Adicionais:**
        * Formato da Resposta: Json
            
        * Requer Autenticação: Não

- #### **GET /provas/aplicacao/<int:id_prova>**
        Retorna uma prova específica com suas questões
        e suas alternativas para que possa ser aplicada.

    #### **URL:** 
      > http://localhost/provas/aplicacao/1
        
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição**:
          A requisição feita a URL deve feito 
          contendo o identificador da prova 
          na URL via querystring.
          
    #### **Parâmetros:**

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_prova | ***sim*** | Identificador da prova no banco de dados | ***Inteiro*** |
    &nbsp;

    #### **Informaçoes Adicionais:**
    
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não

- #### **GET /calculo/notas/aluno/<int:id_aluno>/provas/<int:id_prova>**
        Calcula a nota de um aluno em uma prova
        específica.
  
    #### **URL:** 
    > http://localhost/calculo/notas/aluno/1/provas/1
      
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***GET***


    #### **Estrutura da Requisição:**

          A requisição feita a URL necessita 
          de dois parâmetros que são 
          enviados via queryString.
    
    #### **Parâmetros:**

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro*** |
    | id_prova | ***sim*** | Identificador da prova no banco de dados | ***Inteiro***
    
    &nbsp;
    
    #### **Informaçoes Adicionais:**
            
          * Formato da Resposta: Json
                  
          * Requer Autenticação: Não

- #### **GET /consulta/notas/aluno/<int:id_aluno>**
        Retorna a nota de um aluno específico do 
        banco de dados.

    #### **URL:** 
    > http://localhost/consulta/notas/aluno/1
    
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição**:
          A requisição feita a URL 
          deve apenas ter o identificado do 
          aluno com querystring.
          
    #### **Parâmetros:**

    | Nome | Obrigatório | Descrição | Tipo |
    | ------------- | :-----:| :--------:| :-------: |
    | id_aluno | ***sim*** | Identificador do aluno no banco de dados | ***Inteiro*** |

    &nbsp; 

    #### **Informaçoes Adicionais:**
            
          * Formato da Resposta: Json
                  
          * Requer Autenticação: Não

- #### **GET /consulta/notas/alunos/**
        Retorna todas as notas de alunos do 
        banco de dados.
    #### **URL:** 
      > http://localhost/consulta/notas/alunos/
      
    #### **Métodos HTTP:**
    > Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição:**
        
        A requisição feita a URL não necessita ter uma forma específica.

    #### **Informaçoes Adicionais:**
          
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não

- #### **GET /calculo/notas_finais/aluno/<int:id_aluno>**

        Calcula a nota final de um aluno específico.
  
  #### **URL:** 
    > http://localhost/calculo/notas_finais/aluno/1
    
  #### **Métodos HTTP:**
  > Metodos Aceitos:
  > 
  > - ***GET***

  #### **Estrutura da Requisição**:
        A requisição feita a URL 
        deve apenas ter o identificado do 
        aluno com querystring.

  #### **Informaçoes Adicionais:**
          
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não
    
    &nbsp;

- #### **GET /consulta/notas_finais/aluno/<int:id_aluno>**

        Consulta a nota final de um aluno específico.

    #### **URL:** 
    > http://localhost//consulta/notas_finais/aluno/1
      
    #### **Métodos HTTP:**
    >Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição:**
        
        A requisição feita a URL deve apenas ter o identificado do aluno com querystring.

    &nbsp;
    
    #### **Informaçoes Adicionais:**  
          
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não

- #### **GET /consulta/notas_finais/alunos_aprovados**

        Retorna todos os alunos aprovados do banco de dados.

    #### **URL:** 
    > http://localhost//consulta/notas_finais/alunos_aprovados
      
    #### **Métodos HTTP:**
    >Metodos Aceitos:
    > 
    > - ***GET***

    #### **Estrutura da Requisição:**
        
        A requisição feita a URL apenas.

    &nbsp;
    
    #### **Informaçoes Adicionais:**  
          
        * Formato da Resposta: Json
                
        * Requer Autenticação: Não