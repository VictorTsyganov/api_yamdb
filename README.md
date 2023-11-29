# API для yamdb

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

Спринт 10. Командный проект. API для Yamdb.

Сервис YaMDb — база отзывов о фильмах, книгах и музыке.

**Документация для YaMDb**:

http://127.0.0.1:8000/redoc/ 

## Функционал

**Произведения, к которым пишут отзывы**: получить список всех объектов, создать произведение для отзывов, информация об объекте, обновить информацию об объекте, удалить произведение.

**Категории произведений**: получить список всех категорий, создать категорию, удалить категорию.

**Категории жанров**: получить список всех жанров, создать жанр, удалить жанр.

**Отзывы**: получить список всех отзывов, создать новый отзыв, получить отзыв по id, частично обновить отзыв по id, удалить отзыв по id.

**Комментарии к отзывам**: получить список всех комментариев к отзыву по id, создать новый комментарий для отзыва, получить комментарий для отзыва по id, частично обновить комментарий к отзыву по id, удалить комментарий к отзыву по id.

**Пользователи**: получить список всех пользователей, создание пользователя, получить пользователя по username, изменить данные пользователя по username, удалить пользователя по username, получить данные своей учетной записи, изменить данные своей учетной записи.

**JWT-токен**: отправить confirmation_code на переданный email, получение JWT-токена в обмен на email и confirmation_code.


## Установка

1. Клонировать репозиторий:

   ```python
   git clone git@github.com:VictorTsyganov/api_yamdb.git 
   ```

2. Перейти в папку с проектом:

   ```python
   cd api_yamdb/
   ```

3. Установить виртуальное окружение для проекта:

   ```python
   py -3.9 -m venv venv
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
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```python
   cd api_yamdb/
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Заполнить базу данных и запустить проект:

   ```python
   python manage.py uploader
   python manage.py runserver
   ```

## Ресурсы

```python
# Документаия проекта
http://127.0.0.1:8000/redoc/
```

```python
# ПО для тестирования API, Postman
https://www.postman.com/
```

## Системные требования
- Python 3.7+
- Works on Linux, Windows, macOS

## Стек технологий

- Python 3.7

- Django 3.2

- DRF

- JWT

## Авторы

[Александр Лапп](https://github.com/rogty20) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[Виктор Цыганов](https://github.com/VictorTsyganov) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[Екатерина Рагуткина](https://github.com/R27Kate) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

# Работа с загрузкой данных из csv файлов в базу данных.

* Для удаления имеющихся записей из базы данных, необходимо в командной строке, из дериктории, в которой находится файл manage.py, запустить команду *python manage.py uploader --delete-existing*.
* Для справки - *python manage.py uploader -h или --help*.
* Для загрузки данных из csv файлов в базу данных, необходимо в командной строке, из дериктории, в которой находится файл manage.py, запустить команду *python manage.py uploader*.
* При возникновении ошибок, данные о них будут отражены в терминале.
