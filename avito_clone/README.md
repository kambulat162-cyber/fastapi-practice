# Avito Clone API

Учебный REST API для пользователей, категорий, объявлений, сообщений, заказов
и платежей. Объявление используется как товар в заказе. Платежи сохраняются
в базе в тестовом режиме и не списывают реальные деньги.

## Запуск

Из папки `avito_clone` выполните:

```console
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Документация API будет доступна по адресу `http://127.0.0.1:8000/docs`.
По умолчанию используется SQLite-файл `avito_clone.db`. Путь к базе можно
переопределить переменной `DATABASE_URL`.

Основные маршруты: `/api/v1/users`, `/api/v1/categories`, `/api/v1/ads`,
`/api/v1/search`, `/api/v1/messages`, `/api/v1/orders` и `/api/v1/payments`.

В учебной версии нет авторизации и реального платежного провайдера.
