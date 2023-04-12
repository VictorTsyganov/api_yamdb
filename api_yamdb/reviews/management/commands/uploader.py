import csv
import sqlite3
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    FILES_DATA = {
        'category.csv': 'reviews_category',
        'comments.csv': 'reviews_comment',
        'genre_title.csv': 'reviews_genretitle',
        'genre.csv': 'reviews_genre',
        'review.csv': 'reviews_review',
        'titles.csv': 'reviews_title',
        'users.csv': 'reviews_user'
    }

    def handle(self, *args, **options):
        for file_csv, table_db in self.FILES_DATA.items():
            con = sqlite3.connect('db.sqlite3')
            cur = con.cursor()
            with open(settings.DATA_DIR / file_csv,
                      'r', encoding='utf-8') as file:
                reader = list(csv.reader(file))
                header = tuple(reader[0])
                for j in range(1, len(reader)):
                    for i in range(len(reader[j])):
                        if reader[j][i].isdigit():
                            reader[j][i] = int(reader[j][i])
                    try:
                        cur.execute(
                            f'INSERT INTO {table_db}{header}'
                            f' VALUES {tuple(reader[j])};')
                    except Exception as err:
                        print(
                            f'Строка {tuple(reader[j])} из файла {file_csv}'
                            f' не была загружена в БД. Ошибка: {err}')
            con.commit()
            con.close()
            print(
                f'Загрузка данных из файла {file_csv}'
                f' в таблицу {table_db} завеншена.'
                ' Данные об ошибках см. выше.')
        print('Загрузка всех данных в базу завершена.')
