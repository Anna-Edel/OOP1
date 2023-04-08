import pprint
cook_book = {}

with open('recipes.txt', 'rt', encoding="utf-8") as file:
    for n in file:
        dish_name = n.strip()
        new_list = []
        count = file.readline()
        for i in range(int(count)):
            dish_ing = file.readline()
            ingredient_name, quantity, measure = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish_name: new_list}
        separate = file.readline()
        cook_book.update(dep)


def get_shop_list_by_dishes(dishes, person_count):
    list_of_required_products = {}
    for dish in dishes:
        if dish in cook_book:
            dish_list = {}
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in dish_list:
                    dish_list = {ingredient['ingredient_name']: {'measure': ingredient['measure'],
                                                                 'quantity': ingredient['quantity']}}
                else:
                    person = int(ingredient['quantity']) * person_count
                    dish_list = {ingredient['ingredient_name']: {'measure': ingredient['measure'],
                                                                 'quantity': person}}
                    list_of_required_products.update(dish_list)
    return list_of_required_products


pp = pprint.PrettyPrinter(indent=10)
pp.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
