Гайд по запуску приложения:
1) Сконируйте репозиторий:
```
git clone https://github.com/Tarasyonok/test-task-analytic-solutions
```

2) Создайте образ:
```
docker compose build
```

3) Запустите образ:
```
docker compose up
```

4) Откройте в браузере localhost:8000/docs. Здесь расположена Swagger документация.
GET /api/documents?search_text=Привет - Поиск документов по фразе
DELETE /api/documents/10 - Удаление документа по id
POST /api/documents/load_data - Загрузка тестовых данных в базу данных (сделано для удобства проверки)
