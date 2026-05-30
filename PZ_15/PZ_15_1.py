# Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
# Преподавательский состав должна содержать следующие данные: Табельный номер,
# Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.

import sqlite3
from typing import Optional

import data as data


class Database:
    @staticmethod
    def initialize():
        with sqlite3.connect(data.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                card_number INTEGER PRIMARY KEY,
                name TEXT,
                birthday DATE,
                role TEXT CHECK(role IN ('director', 'zavuch', 'regular')),
                academic_degree TEXT CHECK(academic_degree IN ('academic', 'doctor')),
                workload INTEGER,
                salary INTEGER
            )
            """)

    @staticmethod
    def insert_data():
        with sqlite3.connect(data.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany('INSERT OR IGNORE INTO teachers VALUES(?, ?, ?, ?, ?, ?, ?)', data.DB_DATA)

    @staticmethod
    def print_data(data: list):
        for i in data:
            print(i)

    @staticmethod
    def get_data(card_number: Optional[str] = None, name: Optional[str] = None, role: Optional[str] = None):
        with sqlite3.connect(data.DB_PATH) as conn:
            cursor = conn.cursor()

            if card_number:
                cursor.execute("SELECT * FROM teachers WHERE card_number=?", (card_number, ))
            elif name:
                cursor.execute(f"SELECT * FROM teachers WHERE name=?", (name, ))
            elif role:
                cursor.execute(f"SELECT * FROM teachers WHERE role=?", (role, ))
            else:
                cursor.execute('SELECT * FROM teachers')
            return cursor.fetchall()

    @staticmethod
    def delete_data(card_number: Optional[str] = None, name: Optional[str] = None, role: Optional[str] = None):
        with sqlite3.connect(data.DB_PATH) as conn:
            cursor = conn.cursor()
            if card_number:
                cursor.execute(f"DELETE FROM teachers WHERE card_number=?", (card_number, ))
            elif name:
                cursor.execute(f"DELETE FROM teachers WHERE name=?", (name, ))
            elif role:
                cursor.execute(f"DELETE FROM teachers WHERE role=?", (role, ))
            if cursor.rowcount > 0:
                print("Удалено успешно")
            else:
                print("Записи не найдены")

    @staticmethod
    def update_data(card_number: str, role: Optional[str] = None, academic_degree: Optional[str] = None,
                    salary: Optional[str] = None):
        with sqlite3.connect(data.DB_PATH) as conn:
            cursor = conn.cursor()
            if role:
                cursor.execute(f"UPDATE teachers SET role=? WHERE card_number=?", (role, card_number))
            elif academic_degree:
                cursor.execute(f"UPDATE teachers SET academic_degree=? WHERE card_number=?", (academic_degree, card_number))
            elif salary:
                cursor.execute(f"UPDATE teachers SET salary=? WHERE card_number=?", (salary, card_number))
            if cursor.rowcount > 0:
                print("Обновлено успешно")
            else:
                print("Записи не найдены")


def main():
    Database.initialize()
    Database.insert_data()

    while True:
        print("""
Приложение КАФЕДРА
1 - Поиск (по табельному номеру, фамилия и.о., должности)
2 - Удаление (по табельному номеру, фамилия и.о., должности)
3 - Редактирование (должность, ученая степень, зарплата)""")
        number = input('Выберите действие: ')

        if number == '1':
            choise = input('Варианты поиска: 1 - по табельному номеру, 2 - фамилия и.о., 3 - должности, 4 - найти всех: ')
            if choise == '1':
                Database.print_data(Database.get_data(card_number=input("Введите номер: ")))
            elif choise == '2':
                Database.print_data(Database.get_data(name=input("Введите Фамилия и.о.: ")))
            elif choise == '3':
                Database.print_data(Database.get_data(role=input("Введите роль (director/zavuch/regular): ")))
            elif choise == '4':
                Database.print_data(Database.get_data())

        elif number == '2':
            choise = input('Варианты удаления: 1 - по табельному номеру, 2 - фамилия и.о., 3 - должности: ')
            if choise == '1':
                Database.delete_data(card_number=input("Введите номер: "))
            elif choise == '2':
                Database.delete_data(name=input("Введите Фамилия и.о.: "))
            elif choise == '3':
                Database.delete_data(role=input("Введите роль (director/zavuch/regular): "))

        elif number == '3':
            card_number = input("Введите табельный номер преподавателя: ")
            results = Database.get_data(card_number=card_number)
            if not results:
                print("Преподаватель не найден")
                continue
            Database.print_data(results)
            choise = input('Что редактировать: 1 - должность, 2 - ученая степень, 3 - зарплата: ')
            if choise == '1':
                Database.update_data(card_number, role=input("Новая должность (director/zavuch/regular): "))
            elif choise == '2':
                Database.update_data(card_number, academic_degree=input("Новая степень (academic/doctor): "))
            elif choise == '3':
                Database.update_data(card_number, salary=input("Новая зарплата: "))


if __name__ == '__main__':
    main()
