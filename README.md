# Azure FastAPI Web API – Deploy via GitHub Actions & ACR

![Status do Deploy](https://github.com/Jcnok/azure-web-api/actions/workflows/deploy.yml/badge.svg?branch=master)
![Azure](https://img.shields.io/badge/Azure-WebApp-blue)
![Docker](https://img.shields.io/badge/Docker-Container-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

Este projeto implementa uma API Python com FastAPI, empacotada via Docker e publicada em um Azure Web App usando Azure Container Registry (ACR). O pipeline de CI/CD é automatizado com GitHub Actions, permitindo entregas contínuas de novas versões a cada push.

***

## ⚡️ CI/CD & Status do Deploy

- **Pipeline:** GitHub Actions automatiza o build, push da imagem para o ACR e o deploy para o Azure Web App.
- **Triggers:** Qualquer push na branch principal (`master`) inicia o fluxo de automação e atualização do app.
- **Status:**  
  [![Status do Deploy](https://github.com/Jcnok/azure-web-api/actions/workflows/deploy.yml/badge.svg)](https://github.com/Jcnok/azure-web-api/actions/workflows/deploy.yml)  

***

## 📦 Visão Geral

- **Framework:** FastAPI (Python 3.11)
- **Containerização:** Docker
- **Registry:** Azure Container Registry (ACR)
- **Infra:** Azure Web App Linux
- **Automação:** GitHub Actions
- **Deploy:** Automático via workflow a cada push

***

## 🛠️ Setup e Implantação

### Pré-requisitos

- Conta Azure (Web App + ACR)
- Azure CLI para configurar credenciais
- Secrets configurados no GitHub (`ACR_USERNAME`, `ACR_PASSWORD`, `AZURE_WEBAPP_PUBLISH_PROFILE`)

### Pipeline (deploy.yml)

```yaml
on:
  push:
    branches: [master]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: docker build -t webappdio.azurecr.io/fastapi-webapp:latest .
      - uses: azure/docker-login@v2
        with:
          login-server: webappdio.azurecr.io
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}
      - run: docker push webappdio.azurecr.io/fastapi-webapp:latest
      - uses: azure/webapps-deploy@v2
        with:
          app-name: jconwebapp
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          images: webappdio.azurecr.io/fastapi-webapp:latest
```

***

## 📋 Endpoints

- `GET /` — Retorna mensagem "Olá, Azure!"

***

## 🌐 Endereço de produção

Acesse:  
[`https://jconwebapp.azurewebsites.net`](https://jconwebapp.azurewebsites.net)

***

## 👨‍💻 Autor

**Julio Okuda**  
[LinkedIn](https://www.linkedin.com/in/juliookuda/)

***

**Nota:** Se mudar o nome do arquivo do workflow, adapte o link do badge para:  
```
https://github.com/<usuario>/<repo>/actions/workflows/<nome_do_workflow>.yml/badge.svg?branch=<branch>
```

