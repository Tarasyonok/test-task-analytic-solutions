### Гайд по запуску приложения:
1) Сконируйте репозиторий:
```
git clone https://github.com/Tarasyonok/test-task-analytic-solutions
```

2) Перейдите в папку с приложением:
```
cd test-task-analytic-solutions
```

3) Создайте образ:
```
docker compose build
```

4) Запустите образ:
```
docker compose up
```

5) Откройте в браузере [localhost:8000/docs](localhost:8000/docs). Здесь расположена Swagger документация.  
  * `GET /api/documents?search_text=Привет` - Поиск документов по фразе
  * `DELETE /api/documents/10` - Удаление документа по id
  * `POST /api/documents/load_data` - Загрузка тестовых данных в базу данных (сделано для удобства проверки)


### Для запуска тестов надо
1) Создать виртуальное окружение в папке с приложением:
```
python -m venv venv
```

2) Активировать виртуальное окружение:
```
./venv/Scripts/activate
```

3) Установить зависимости:
```
pip install -r requirements.txt
```

4) Создать базы данных в PostgreSQL для разработки и тестировани, и создать .env файл скопировав содержимое файла .env-example.

5) Прогнать тесты:
```
pytest -v -s
```
