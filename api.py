import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/Teste")
def exemple() -> str:
    return "ola mundo"


if __name__ == "__main__":
    uvicorn.run(app, port=8000)