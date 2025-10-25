from fastapi import FastAPI 
import time

app = FastAPI()
# Timestamp de início para tracking
start_time = time.time()

@app.get("/")
def read_root():
  return{"mensagem":"Deploy da FastAPI com Azure Web Service com CI/CD realizada com sucesso após ativar a implantação contínua!!!"}

@app.get("/health")
def health_check(): 
  uptime = time.time() - start_time
  return {
      "status": "healthy",
      "service": "fastapi-webapp",
      "uptime_seconds": int(uptime)}