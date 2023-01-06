import sqlite3
import random

from ingridients import proteins, carbs, fats, fiber


base = sqlite3.connect("makemenu.db", check_same_thread=False)
sql = base.cursor()


def random_ingridient(ingridient, quantity):
    result = set()
    while len(result) < quantity:
        result.add(ingridient[random.randrange(len(ingridient))])
    return list(result)

# print(random_ingridient(fats, 5))


def make_plate(quantity):
    result = []
    for i in range(quantity):
        result.append([  
        proteins[random.randrange(len(proteins))],        
        carbs[random.randrange(len(carbs))],
        fats[random.randrange(len(fats))],
        fiber[random.randrange(len(fiber))]]
        )
    return result



def make_uniqu_plates(quantity):
    result = []
    protein = random_ingridient(proteins, quantity)
    carb = random_ingridient(carbs, quantity)
    fat = random_ingridient(fats, quantity)
    fiber_ing = random_ingridient(fiber, quantity)
    for i in range(quantity):
        result.append([protein[i], carb[i], fat[i], fiber_ing[i]])
    return result

# print(make_uniqu_plates(3))


def make_menu(quantity):
    result = []
    ingridients_for_menu = []
    ingridients_for_menu.append([
        random_ingridient(proteins, quantity),
        random_ingridient(carbs, quantity),
        random_ingridient(fats, quantity),
        random_ingridient(fiber, quantity)
        ])
    print(ingridients_for_menu)
    for i in range(quantity):
        for k in range(4):
            result.append(ingridients_for_menu[0][k][i])

    return result





# def check_db_exists():
#     """Проверяет наличие основной таблицы, если её нет - создаёт """
#     sql.execute("""CREATE TABLE IF NOT EXISTS expenses (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 owner_id INTEGER,
#                 user TEXT,
#                 expense INTEGER,
#                 comment TEXT,
#                 date timestamp)""")
#     base.commit()


# def check_table_exists():
#     """ Проверяем наличие таблицы Юзеров, если не существует - создаём """
#     sql.execute("""CREATE TABLE IF NOT EXISTS owners (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 owner_id INTEGER,
#                 owner_name TEXT)""")
#     base.commit()


# check_db_exists()
# check_table_exists()

# CREATE TABLE "proteins" ( "id" INTEGER, "name" TEXT, "category" TEXT, "weights" INTEGER, "heiters" INTEGER, "incompatible" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )