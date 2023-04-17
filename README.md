# API для yamdb

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

Спринт 10. Командный проект. API для Yamdb.

## Функционал


## Установка

1. Клонировать репозиторий:

   ```python
   git clone 
   ```

2. Перейти в папку с проектом:

   ```python
   cd api_yamdb/
   ```

3. Установить виртуальное окружение для проекта:

   ```python
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate
   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```python
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```python
   cd yatube
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

7. Запустить проект:

   ```python
   python manage.py runserver
   ```

## Примеры запросов

Создание отзыва

Комментирование отзыва

## Ресурсы

```python
# Документаия проекта
http://127.0.0.1:8000/redoc/
```

```python
# ПО для тестирования API, Postman
https://www.postman.com/
```

## Авторы

# Описание

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

http://127.0.0.1:8000/redoc/ Документация для YaMDb

# Системные требования
- Python 3.7+
- Works on Linux, Windows, macOS

# Стек технологий

- Python 3.7

- Django 3.2

- DRF

- JWT

# api_yamdb
api_yamdb

# Работа с загрузкой данных из csv файлов в базу данных.

* Для удаления имеющихся записей из базы данных, необходимо в командной строке, из дериктории, в которой находится файл manage.py, запустить команду *python manage.py uploader --delete-existing*.
* Для справки - *python manage.py uploader -h или --help*.
* Для загрузки данных из csv файлов в базу данных, необходимо в командной строке, из дериктории, в которой находится файл manage.py, запустить команду *python manage.py uploader*.
* При возникновении ошибок, данные о них будут отражены в терминале.
