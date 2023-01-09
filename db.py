import sqlite3

from ingridients import proteins, carbs, fats, fiber

base = sqlite3.connect("makemenu.db", check_same_thread=False)
sql = base.cursor()


def create_ingridient_table(ingridient):
    """ Проверяем наличие таблицы ингридиентов, если не существует - создаём """
    sql.execute(f"""CREATE TABLE IF NOT EXISTS {ingridient} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT DEFAULT 'Undefined',
                weights INTEGER DEFAULT 50,
                heiters INTEGER DEFAULT 0,
                incompatible TEXT DEFAULT 'Undefined')""")
    base.commit()

create_ingridient_table('proteins')
create_ingridient_table('carbs')
create_ingridient_table('fats')
create_ingridient_table('fiber')


# def insert_ingridients_to_table(ingridients):
#     for ingridient in ingridients:
#         print(ingridient)
#         # sql.execute(f'INSERT INTO proteins (name) VALUES(?)', (ingridient,))
#         # sql.execute(f'INSERT INTO carbs (name) VALUES(?)', (ingridient,))
#         # sql.execute(f'INSERT INTO fats (name) VALUES(?)', (ingridient,))
#         sql.execute(f'INSERT INTO fiber (name) VALUES(?)', (ingridient,))
#         base.commit()



# insert_ingridients_to_table(fiber)