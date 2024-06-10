
# Mercadinho

Se trata de uma api feita em fast api com elementos crud, onde e possivel registrar, atualizar, acessar e excluir produtos.


## Documentação da API



#### Criar um novo produto

Método HTTP: POST
Endpoint: /products/
Descrição: Cria um novo produto.
Parâmetros:

product (CreateProduct, obrigatório): Os dados do produto a ser criado.

db (Session, dependência obrigatória): A sessão do banco de dados.

Exemplo de Requisição:
{
  "name": "Nome do Produto",
  "Quantity": "4",
  "price": 100.0
}


#### Retorna um produto específico pelo ID
Método HTTP: GET
Endpoint: /products/{product_id}
Descrição: Retorna um produto especifico pelo ID.
Parâmetros:

product_id (int, obrigatório): O ID do produto que você quer.

db (Session, dependência obrigatória): A sessão do banco de dados.

#### Retornar todos os produtos
Método HTTP: GET
Endpoint: /products/
Descrição: Retorna a lista completa de produtos.
Parâmetros:

db (Session, dependência obrigatória): A sessão do banco de dados.


#### Atualizar um produto
HTTP: PUT
Endpoint:/products/{product_id}
Descrição: Usado para atualizar um produto existente.
Parâmetros:

product_id (int, obrigatório): O ID do produto que você quer atualizar.

product (CreateProduct, obrigatório): Os dados atualizados do produto.

db (Session, dependência obrigatória): A sessão do banco de dados.

Exemplo requisição:
{
  "name": "Novo nome",
  "Quantity": "2",
  "price": 150.0
}

#### Deletar um produto 
Método HTTP: DELETE
Endpoint: /products/{product_id}
Descrição: Deleta o produto especificado.
Parâmetros:

product_id (int, obrigatório): O ID do produto que você quer deletar.

db (Session, dependência obrigatória): A sessão do banco de dados.












## Documentação

Contribuidores:


## Luís Cardoso


Fiquei responsável por gerenciar a equipe e auxiliar todos como o líder do projeto, através disso fiz uso do conhecimento abordado em sala pra auxiliar aqueles que tiveram dificuldades com o uso do github e  do docker, também separei a função pra cada um com base em suas aptidões para assim ter uma melhor perfomance na hora de desenvolver o código, também ajudei em algumas correções no código que estavam dando erros e fiz testes para verificar seu funcionamento.


## Lucas Emanuel Dias dos Santos Oliveira

Assumi uma responsabilidade significativa em diversas áreas, Inicialmente fui responsável pela criação da estrutura básica do sistema,Para que meu grupo pudesse começar o projeto adequadamente . Além disso, desenvolvi o Docker para o mercadinho, configurando os contêineres e otimizando o ambiente. Também desempenhei um papel crucial na criação das funções CRUD, colaborando e auxiliando com a equipe para garantir que as operações com banco de dados estivessem funcionando corretamente.
Ps: também criei este arquivo readme 


## BRUNO MARCEL

Minha responsabilidade foi documentar 2 partes essenciais do projeto: módulo routers e módulo schemas da aplicação. 

Documentação dos Routers

A documentação do arquivo some_router.py foi um dos principais focos. Este arquivo define as rotas da API relacionadas ao gerenciamento de produtos, utilizando o framework FastAPI.

Criação de Produto: Expliquei como a aplicação permite a criação de novos produtos através de uma rota específica que aceita dados de entrada e retorna o produto criado.

Leitura de Produtos: Documentei as rotas que permitem obter tanto uma lista de produtos quanto um produto específico pelo seu ID, detalhando como a aplicação recupera esses dados do banco de dados.

Atualização de Produto: Descrevi o processo de atualização de um produto existente, explicando a rota e como os dados são validados e persistidos no banco de dados.

Exclusão de Produto: Documentei a rota que permite deletar um produto, incluindo o tratamento de exceções caso o produto não seja encontrado.

Documentação dos Schemas

Além dos routers, também documentei o arquivo principal dos schemas. Os schemas são responsáveis pela validação dos dados que entram e saem da aplicação, garantindo que a API manipule apenas dados corretos e no formato esperado.




## Juan Nascimento

Minha função neste projeto foi desenvolver as rotas da nossa API. Fiquei responsável por implementar as seguintes funcionalidades:

create_product: Rota responsável pela criação de novos produtos e pelo cadastro dos mesmos no banco de dados.

read_product: Rota que permite a consulta de um produto específico no banco de dados, utilizando seu ID.

read_products: Rota que recupera e lista todos os produtos disponíveis no banco de dados.

update_product: Rota destinada à atualização das informações de um produto específico, identificado pelo seu ID, no banco de dados.

delete_product: Rota que remove um produto do banco de dados com base em seu ID.

## VINCIUS LEITE VIEIRA
 
RESPONSÁVEL PELO O DESENVOLVIMENTO DAS ROTAS DA API:
 
 
Fique responsável por definir as rotas dos produtos que tem por base a maneira que os produtos se comportam na aplicação,
 
Arquivo `routes.py`
 
Essas Rotas são :
 
DELETE/
CADASTRAR /
CRIAR/
 
Cada rota dessas demonstra a forma como a aplicação do produto se comporta na api.
 
 




## ROBERT EVERTHON

Minha função foi realizar a documentação do projeto, especificamente dos módulos main, database, crud_product e product.

Documentação do main:
Na documentação do main, basicamente importamos os módulos, bibliotecas e as classes que fizemos,
criamos uma instância e uma função para executar a oplicação.

Documentação do database:
Aqui documentei a ligação com o banco de dados importando a biblioteca "sqlalchemy",
que contem as ferramentas necessárias para interagir com o banco de dados.

Documentação do product:
coloquei a documentação do "product", aqui é onde se tem as instruções para criar o objeto "produto" que vamos
utilizar no crud.

Documentação do crud_product:
Aqui documentei, o CRUD do produto, que recebe como base a classe product que criamos para adicionar,
buscar, atualizar e procurar os produtos no banco de dados.







"Cada pessoa descreveu sua função conforme seu ponto de vista"


## Instalação e inicialização

Para utilizar a api são necessárias a  instalação de algumas bibliotecas, como o projeto foi feito no docker foi necessário criar um requirement.txt para q instalasse as dependencias no ambiente virtual, felizmente também podemos a utilizar para baixar as bibliotecas na maquina principal

Comando para ir ao diretorio requirements.txt
```
Cd mercadinho-api
```
Comando para baixar as bibliotecas
```
Pip install -r requirements.txt
```
Nessa Api também e necessário possuir o docker instalado para que se possa criar um ambiente virtual

## Inicialização
Com o docker-desktop aberto
Ao entrar no diretorio mercadinho-api
Deve utilizar o comando:

```
docker-compose build
```
Para construir o ambiente virtual.

Em seguida se usa:

```
docker-compose up
```
Para subir o ambiente virtual.

A Partir dai a api ja vai estar funcionando e podera ser acessada por um navegador utilizando o localhost:8000, no caso o localhost:8000/products/ onde os produtos cadastrados estarão 

Sendo possivel adcionar, excluir , atualizar e vizualizar produtos específicos ou não com comandos no powershell.

Comandos esses disponíveis no diretorio:
```
Mercadinho-api/crud coments.txt
```







    