from fastapi import FastAPI 


app = FastAPI()

@app.get("/")
def read_root():
  return{"mensagem":"Deploy da api com Azure Web Service com CI/CD realizada com sucesso após ativar a implantação contínua!!!"}
