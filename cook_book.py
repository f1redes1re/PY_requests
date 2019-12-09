# Домашнее задание к лекции 2.4 «Открытие и чтение файла, запись в файл»
# Задача №1


def create_cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf8') as rec:
        for line in rec:
            ingredient_title = line.strip()
            if ingredient_title != '':
                ingredient_counter = []
                ingredient_quantity = int(rec.readline().strip())
                for i in range(ingredient_quantity):
                    ingredient_parse = rec.readline().strip().split(' | ')
                    ingredients_list = {'ingridient_name': ingredient_parse[0],
                                        'quantity': int(ingredient_parse[1]),
                                        'measure': ingredient_parse[2]}
                    ingredient_counter.append(ingredients_list)
                cook_book[ingredient_title] = ingredient_counter

# Задача №2

    person_count = int(input('Сколько персон: '))
    dishes = input('Что будем есть? (перечисление - через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            add_shop_list_item = dict(ingridient)
            add_shop_list_item['quantity'] *= person_count
            if add_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[add_shop_list_item['ingridient_name']] = add_shop_list_item
            else:
                shop_list[add_shop_list_item['ingridient_name']]['quantity'] += add_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    print('Список покупок в магазне: ')
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'],
                                shop_list_item['quantity'],
                                shop_list_item['measure']))


create_cook_book()
