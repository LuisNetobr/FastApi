#define a imagem base do Python 3.10 slim que se trata uma versão mais leve do Python
FROM python:3.10-slim

#cria um diretorio de trabalho code no docker
WORKDIR /code

#Usado para definir as variáveis de ambiente para desabilitar a escrita de bytecode (.pyc) e tambem para garantir que o stderr e  stdout  sejam descarregados sem buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Comando para atualizar a lista de pacotes e instala gcc e musl-dev sem pacotes recomendados adicionais afim de reduzir o tamanho da imagem
RUN apt-get update && apt-get install -y --no-install-recommends gcc musl-dev

#Esse comando Adiciona o caminho do ambiente virtual ao PATH para garantir que todas as chamadas de Python e pip usem o ambiente virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#Comando ultilizado para atualiza o pip no ambiente virtual
RUN /opt/venv/bin/pip install --upgrade pip

#Comando para copiar o requirements,txt para o diretorio do docker
COPY requirements.txt .

#Comando ultilizado ara instala as dependências do projeto
RUN pip install -r requirements.txt

#Comando para copiar o diretorio inteiro atual do host para o diretório "code" no docker
COPY . .

#Comando para Expor a porta
EXPOSE 8000

# Comando necessario para inicializar a aplicação pela uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]