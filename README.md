
# 🚀 Pipeline DevOps Completo: Do Push ao Deploy na Azure com FastAPI, Docker & GitHub Actions

[![Status do Deploy](https://github.com/Jcnok/azure-web-api/actions/workflows/deploy.yml/badge.svg?branch=master)](https://github.com/Jcnok/azure-web-api/actions/workflows/deploy.yml)
![Azure](https://img.shields.io/badge/Azure-WebApp-blue)
![Docker](https://img.shields.io/badge/Docker-Container-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Tech](https://img.shields.io/badge/Tech-FastAPI|GitHubActions|Azure-blueviolet)

## Sumário

- [🚀 Pipeline DevOps Completo: Do Push ao Deploy na Azure com FastAPI, Docker \& GitHub Actions](#-pipeline-devops-completo-do-push-ao-deploy-na-azure-com-fastapi-docker--github-actions)
  - [Sumário](#sumário)
  - [📦 Visão Geral](#-visão-geral)
  - [🏗️ Arquitetura \& Tecnologias](#️-arquitetura--tecnologias)
  - [💻 Como Rodar Localmente](#-como-rodar-localmente)
  - [🚀 Deploy Automático na Azure](#-deploy-automático-na-azure)
  - [✅ Checklist de Validação](#-checklist-de-validação)
  - [🌟 Boas Práticas \& Lições Aprendidas](#-boas-práticas--lições-aprendidas)
  - [🩺 Troubleshooting](#-troubleshooting)
  - [🔗 Links Úteis](#-links-úteis)
  - [👨‍💻 Autor](#-autor)

## 📦 Visão Geral

Este projeto mostra como construir **um pipeline DevOps de ponta-a-ponta** para publicar APIs Python com FastAPI, empacotadas em Docker e publicadas no Azure via Container Registry. Todo o fluxo de CI/CD está automatizado com GitHub Actions, desde o build até o deploy e atualização contínua do app a cada push.

## 🏗️ Arquitetura & Tecnologias

- **FastAPI** (Python 3.11)
- **Docker** (Containerização)
- **Azure Container Registry** (Armazenamento da imagem)
- **Azure Web App Linux** (Hospedagem)
- **GitHub Actions** (Automação CI/CD)
- **Secrets no GitHub** para credenciais seguras

## 💻 Como Rodar Localmente

1. Instale Docker, Azure CLI e Git.
2. Clone o repositório:
   ```
   git clone https://github.com/Jcnok/azure-web-api.git
   cd azure-web-api
   ```
3. Crie e ative o ambiente virtual:
   ```
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate.bat   # Windows
   pip install -r requirements.txt
   ```
4. Rode o servidor local:
   ```
   uvicorn main:app --reload
   ```
   Acesse [localhost:8000/docs](http://127.0.0.1:8000/docs) para ver a documentação Swagger.

## 🚀 Deploy Automático na Azure

1. Provisionar recursos via Azure CLI (Resource Group, Container Registry, Web App, etc.).
2. Configurar secrets no GitHub: `ACR_USERNAME`, `ACR_PASSWORD`, `AZURE_WEBAPP_PUBLISH_PROFILE`.
3. Cada push na branch `master` dispara o pipeline (workflow) de CI/CD:
   - Build da imagem Docker
   - Push para o ACR
   - Deploy automático para o Web App com Always-On e publish via webhook

4. URL de produção:
   [https://jconwebapp.azurewebsites.net](https://jconwebapp.azurewebsites.net)

## ✅ Checklist de Validação

- [x] API responde na URL pública
- [x] Documentação Swagger disponível em `/docs`
- [x] Push na branch main dispara workflow
- [x] Workflow conclui com badge verde
- [x] Secrets corretamente configurados no GitHub
- [x] Web App no plano B1 (Always-On e Implantação Contínua)
- [x] Imagem Docker disponível no ACR

## 🌟 Boas Práticas & Lições Aprendidas

- Use sempre o plano B1 para o experimento(não use plano gratuito para produção/CICD)
- Nunca commite credenciais; use secrets
- Teste a aplicação localmente antes de containerizar
- Nomes de ACR/WebApp devem ser globais e sem hífens para ACR
- Prefira deployments via webhook para maior confiabilidade

## 🩺 Troubleshooting

- **Application Error:** Quase sempre é porta. Verifique EXPOSE 8000 e config no Web App.
- **Secrets inválidos no login:** Verifique credenciais ACR.
- **Deploy OK, mas não atualiza:** Webhook pode não estar ativo, ou plano F1 está suspenso.
- [Documentação oficial Azure Web App](https://docs.microsoft.com/pt-br/azure/app-service/)
- [Documentação FastAPI](https://fastapi.tiangolo.com/)

## 🔗 Links Úteis

- [Repositório GitHub](https://github.com/Jcnok/azure-web-api)
- [Guia da Azure CLI](https://docs.microsoft.com/pt-br/cli/azure/)

## 👨‍💻 Autor

**Julio Okuda**  
[LinkedIn](https://www.linkedin.com/in/juliookuda/)  

---

**Pronto para turbinar seus projetos?**  
Clone, experimente, contribua ou conecte-se para discutir melhorias ou parcerias!

