import sqlite3

base = sqlite3.connect("makemenu.db", check_same_thread=False)
sql = base.cursor()


def create_ingridient_table(ingridient):
    """ Проверяем наличие таблицы ингридиентов, если не существует - создаём """
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {ingridient} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                weights INTEGER,
                heiters INTEGER,
                incompatible TEXT)""")
    base.commit()

create_ingridient_table('proteins')
create_ingridient_table('carbs')
create_ingridient_table('fats')
create_ingridient_table('fiber')