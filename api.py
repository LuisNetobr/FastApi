'''IMPORTAÇÕES:'''
import uvicorn '''Importamos a biblioteca "uvicorn" para criar um servidor web para hospedar a aplicação.'''
from fastapi import FastAPI '''Importamos o framework fastAPI.'''

from fastapi import FastAPI, Depends, HTTPException '''O "Depends" serve para colocar dependências nas
funções de rota, e o "HTTPException" serve para gerar exceções HTTP.'''

from sqlalchemy import create_engine '''Importamos a função "create_engine" de "sqlalchemy" para conectar
a aplicação com o banco de dados.'''

from sqlalchemy.orm import Session '''Por fim, importamos do módulo "sqlalchemy.orm" a classe "Session", 
que vai funcionar como intermediadora entre as interações da aplicação com o banco de dados.'''

'''-------------------------------------------------------------------------------------------------------------------'''
'''FUNÇÕES:'''

app = FastAPI()'''É criada a instância do fastAPI'''

@app.post("/CadastrarProdutos", status_code=201)''' Com o "@app.post("/CadastrarProdutos"), criamos uma rota para
 "cadastrar_Produto", e o parâmetro  HTTP 201, indica que a requisição do usuário foi bem sucedida. '''

def cadastrar_produto(produto: Produto, db: Session = Depends(get_db)):'''Criamos a função de
 "cadastrar_produto" que recebe de parâmetros o "produto" e o "db(banco de dados)"'''
    try:
        novo_produto = Produto(**produto.dict())'''Criamos o "novo produto" com base no valor digitado no
parâmetro "produto", **produto.dict() serve para desempacotar converter esse valor do produto em dicionário '''
        
        db.add(novo_produto)'''Adiciona um novo produto ao banco de dados'''
        db.commit()'''Comitamos as alterações no banco de dados'''
        return {"mensagem": "Produto cadastrado com sucesso!"}''' Se o cadastro do produto for bem sucedido, mostra a "mensagem")'''
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao cadastrar produto")'''Se o cadastro do produto não for bem sucedido,
        mostra a "mensagem"'''


@app.get("/ListarProdutos")
def listar_produtos(db: Session = Depends(get_db)):
    try:
        produtos = db.query(Produto).all()
        return produtos
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao listar produtos")

@app.put("/AtualizarProdutos/{produto_id}")
def atualizar_produto(produto_id: int, produto: Produto, db: Session = Depends(get_db)):
    try:
        produto_db = db.query(Produto).filter(Produto.id == produto_id).first()
        if not produto_db:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        produto_db.update(produto.dict())
        db.commit()
        return {"mensagem": "Produto atualizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao atualizar produto")

@app.delete("/DeletarProdutos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    try:
        produto_db = db.query(Produto).filter(Produto.id == produto_id).first()
        if not produto_db:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        db.delete(produto_db)
        db.commit()
        return {"mensagem": "Produto deletado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao deletar produto")


@app.get("/Teste")
def exemple() -> str:
    return "ola mundo"


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
