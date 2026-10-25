# FastAPI — практика

Примеры по первым 5 статьям [руководства metanit](https://metanit.com/python/fastapi/) и учебное API пользователей со Swagger.

## Установка

```
pip install -r requirements.txt
```

## Примеры по урокам

| Файл | Тема | Запуск |
|---|---|---|
| `lesson1_first_app.py` | Что такое FastAPI, первое приложение | `uvicorn lesson1_first_app:app --reload` |
| `lesson2_requests.py` | Класс FastAPI и обработка запроса | `uvicorn lesson2_requests:app --reload` |
| `lesson3_responses.py` | Отправка ответа (Response, HTML, текст, JSON) | `uvicorn lesson3_responses:app --reload` |
| `lesson4_files.py` | Отправка файлов (FileResponse) | `uvicorn lesson4_files:app --reload` |
| `lesson5_path_params.py` | Параметры пути и валидация через Path | `uvicorn lesson5_path_params:app --reload` |

После запуска открыть http://127.0.0.1:8000

## API пользователей (`users_api.py`)

```
uvicorn users_api:app --reload
```

Swagger: http://127.0.0.1:8000/docs

| Метод | Адрес | Что делает |
|---|---|---|
| GET | `/users` | список пользователей |
| GET | `/users/{user_id}` | один пользователь |
| POST | `/users` | создать |
| PUT | `/users/{user_id}` | изменить |
| DELETE | `/users/{user_id}` | удалить |

Пример тела для POST / PUT:

```json
{
  "name": "Max",
  "age": 19,
  "email": "max@mail.ru"
}
```

Swagger UI настроен через `swagger_ui_parameters` ([документация](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)): тёмная тема подсветки, время запроса, сразу включённая кнопка «Try it out».

Данные хранятся в списке в памяти — после перезапуска сервера всё сбрасывается.
