# TaskBoard

TaskBoard is a small task management REST API built with FastAPI, used as the base project for the DevSecOps course at ESIEE Paris. It exposes CRUD endpoints to create, list, read, update and delete tasks.

## Requirements

- Python 3.11 or newer
- Git

## Installation

```bash
git clone git@github.com:Azhrod/taskboard.git
cd taskboard
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

The API is available at http://127.0.0.1:8000 and the interactive documentation (Swagger UI) at http://127.0.0.1:8000/docs.

## Tests

```bash
python -m pytest -v
```

## Environment variables

Copy `.env.example` to `.env` and fill in your own values:

```bash
cp .env.example .env      # Windows: copy .env.example .env
```

Never commit `.env`: it is listed in `.gitignore`. Only `.env.example`, which contains placeholder values, belongs in the repository.

| Variable | Description |
| --- | --- |
| `APP_ENV` | Environment name (`development`, `production`) |
| `LOG_LEVEL` | Logging level (`info`, `debug`, ...) |
| `DATABASE_URL` | Database connection string (used in a later session) |
| `SECRET_KEY` | Application secret key |

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Health check |
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | List all tasks |
| `GET` | `/tasks/{task_id}` | Get a task by ID |
| `PATCH` | `/tasks/{task_id}` | Update the fields sent |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

## Project structure

```
taskboard/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application and health check
│   ├── schemas.py         # Pydantic models
│   └── routers/
│       ├── __init__.py
│       └── tasks.py       # /tasks endpoints
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
├── docs/
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```