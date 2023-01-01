from ingridients import proteins, carbs, fats, fiber
import random

def random_ingridient(ingridient, quantity):
    result = set()
    while len(result) < quantity:
        result.add(ingridient[random.randrange(len(ingridient))])
    return list(result)

# print(random_ingridient(fats, 5))


def make_plate(quantity):
    result = []



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



print(make_menu(2))


# print(proteins[random.randrange(len(proteins))])
# print(proteins[random.randrange(len(proteins))])
# print(proteins[random.randrange(len(proteins))])
# print(proteins[random.randrange(len(proteins))])