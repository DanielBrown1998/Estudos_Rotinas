import sqlite3
DAYS = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']


def create_database():
    with sqlite3.connect('data/db.sqlite3') as connection:
        cursor = connection.cursor()
        for day in DAYS:
            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {day}'
                f'('
                f'hour INTEGER PRIMARY KEY,'
                f'texto TEXT'
                f')',
            )
        connection.commit()


def drop_database():
    with sqlite3.connect('data/db.sqlite3') as connection:
        cursor = connection.cursor()
        for day in DAYS:
            cursor.execute(
                f"DROP TABLE {day}"
            )
        connection.commit()


def consult_database(day: str) -> list:
    data = []
    with sqlite3.connect('data/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM {day}"
        )
        data = cursor.fetchall()

    return data


def update_database(day: str, hour: int, texto: str) -> None:

    with sqlite3.connect('data/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE TABLE {day} SET texto = ? WHERE hour = ?',
            (texto, hour)
        )
        connection.commit()


def insert_table(day: str, hour: int, texto: str) -> None:
    with sqlite3.connect('data/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO {day} (texto) VALUES ? where hour=?",
            (texto, hour)
        )

