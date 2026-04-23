# hng14-stage2-devops
# HNG Stage 2 DevOps Project – Full Stack CI/CD System

A full-stack system with a working CI/CD pipeline that goes from linting all the way to deployment.

The goal of this project is simple: take a messy multi-service app and turn it into a properly automated DevOps pipeline that can run anywhere from scratch with minimal effort.

---

## What this project does

This system is made up of:

- FastAPI backend (handles job creation and status tracking)
- Redis (used as a queue system)
- Worker service (processes background jobs)
- Node.js frontend (simple interface to interact with backend)
- GitHub Actions CI/CD pipeline (fully automated workflow)

Flow:
Frontend → Backend → Redis Queue → Worker → Redis → Backend → Frontend

---

## Requirements

Before running this project, make sure you have:

- Docker installed
- Docker Compose installed
- Git installed
- Python 3.8+
- Node.js 18+

---

## How to run this project from scratch

### 1. Clone the repository

```bash
git clone https://github.com/ejalonibudamilola/hng14-stage2-devops
cd hng14-stage2-devops
```

---

### 2. Set environment variables

Create a `.env` file in the root directory:

---

### 3. Start the full system

```bash
docker compose up --build
```

Or run in detached mode:

```bash
docker compose up -d --build
```

---

## Services

- Frontend → http://localhost:3000
- Backend → http://localhost:8000
- Health Check → http://localhost:8000/health

---

## Running tests locally

Backend tests:

```bash
cd api
pytest --cov=api --cov-report=html
```

Linting:

```bash
flake8 api worker tests
```

Frontend lint:

```bash
cd frontend
npx eslint .
```

---

## CI/CD Pipeline

GitHub Actions pipeline runs in this order:

lint → test → build → security scan → integration test → deploy

It ensures:

- No bad code gets merged
- All tests pass before build
- Docker images are scanned for vulnerabilities
- Full system is tested before deployment

---

## What success looks like

When everything is working:

- Backend starts with no errors
- Worker starts processing jobs
- Redis queue is active
- Frontend can submit jobs successfully
- Job status changes from queued → completed

---

## Stop the system

```bash
docker compose down -v
```

---

