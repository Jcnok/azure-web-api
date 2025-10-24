from fastapi import FastAPI 


app = FastAPI()

@app.get("/")
def read_root():
  return{"mensagem":"Deploy da api com Azure Web Service com CI/CD realizada com sucesso após ativar a implantação contínua!!!"}

@app.get("/health")
def health_check():
    uptime = time.time() - start_time
    return {
        "status": "healthy",
        "service": "fastapi-webapp",
        "uptime_seconds": int(uptime)
    }