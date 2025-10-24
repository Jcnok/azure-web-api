from fastapi import FastAPI 


app = FastAPI()

@app.get("/")
def read_root():
  return{"mensagem":"Olá, deploy da api com Azure Web Service realizada com sucesso!!!"}
