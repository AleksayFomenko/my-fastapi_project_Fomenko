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
    ├── requirements.txt   # Зависимости сервиса
    └── Dockerfile         # Docker-образ TODO-сервиса
