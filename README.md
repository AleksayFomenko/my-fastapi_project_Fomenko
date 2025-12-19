# my-fastapi_project_Fomenko
Учебный проект, включающий микросервис на базе **FastAPI**:
- **TODO-сервис** — CRUD-операции для списка задач

TODO-сервис:
- использует SQLite для хранения данных,
- упакован в Docker-контейнер,
- сохраняет данные в именованном Docker-томе,
- имеет автоматическую документацию Swagger (`/docs`).

Структура репозитория:

```text
fastapi-microservices/
└─ todo_service/
    ├── app/
    │   ├── main.py        # Точка входа FastAPI-приложения
    │   ├── database.py    # Работа с SQLite и инициализация БД
    │   └── models.py      # Pydantic-модели
    │   └── data/          # БД-data
    ├── requirements.txt   # Зависимости сервиса
    └── Dockerfile         # Docker-образ TODO-сервиса

Запуск локально:
  docker build -t todo-service:local
  docker volume create todo_data
  docker run --rm -p 8000:80 -v todo_data:/app/data --name todo-service todo-service:local
Через Docker:
  docker run-d-p 8000:80-v todo_data:/app/data <ваш_логин_hub>/todo-service:latest
