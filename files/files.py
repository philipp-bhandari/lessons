from pprint import pprint


def split_line(line):
    line_arr = line.split('|')
    line_arr = [i.strip() for i in line_arr]
    return line_arr


def get_string(file):
    return file.readline().strip()


def is_ingredient(line, index):
    try:
        if line[index]:  # Не придумал другого способа
            pass         # проверить существует ли элемент списка.
        return True
    except IndexError:
        return False


def read_cookbook_file():
    cook_book = {}
    with open('cookbook') as file:
        for line in file:
            cook_name = line.strip()

            get_string(file)  # Пропуск строки с количеством ингредиентов

            ingredient_line = split_line(get_string(file))

            cook_book[cook_name] = []
            while is_ingredient(ingredient_line, 2):
                ingredient = {'ingredient_name': ingredient_line[0],
                              'quantity': ingredient_line[1],
                              'measure': ingredient_line[2]}
                cook_book[cook_name].append(ingredient)
                ingredient_line = split_line(get_string(file))
            continue
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook_file()
    out_dict = {}

    for dish in dishes:
        try:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']

                if name not in out_dict:
                    quantity = float(ingredient['quantity']) * int(person_count)
                    out_dict[name] = {'measure': ingredient['measure'],
                                      'quantity': quantity}
                else:
                    quantity = out_dict[name]['quantity'] + (float(ingredient['quantity']) * int(person_count))
                    out_dict[name] = {'measure': ingredient['measure'],
                                      'quantity': quantity}

        except KeyError:
            print(f'\nБлюда {dish} не найдено.\n')
    return out_dict


def print_cook_book():
    cook_book = read_cookbook_file()

    for cook, ingredients in cook_book.items():
        print(cook)
        for ingredient in ingredients:
            print(ingredient)
        print('\n' + '*' * 3 + '\n')


def print_quantity(dishes, count):
    result = get_shop_list_by_dishes(dishes, count)
    for item, props in result.items():
        pprint(item)
        pprint(props)


print_cook_book()  # Задание 1


print_quantity(['Фахитос', 'Омлет', 'Утка по-пекински'], 4)  # Задание 2
