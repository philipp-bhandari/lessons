def split_line(line):
    line_arr = line.split('|')
    line_arr = [i.strip() for i in line_arr]
    return line_arr


def get_string(file):
    return file.readline().strip()


def is_ingredient(line, index):
    try:
        if line[index] == 1:  # Не придумал другого способа проверить существует ли элемент списка.
            pass
        return True
    except IndexError:
        return False


def exercise_1():
    cook_book = {}
    dish_persons_count = {}
    with open('cookbook') as file:

        for line in file:
            cook_name = line.strip()

            dish_persons_count[cook_name] = get_string(file)  # Для второго задания

            ingredient_line = split_line(get_string(file))

            cook_book[cook_name] = []
            while is_ingredient(ingredient_line, 2):
                ingredient = {'ingredient_name': ingredient_line[0],
                              'quantity': ingredient_line[1],
                              'measure': ingredient_line[2]}
                cook_book[cook_name].append(ingredient)
                ingredient_line = split_line(get_string(file))
            continue
    return cook_book, dish_persons_count


def get_shop_list_by_dishes(dishes, person_count):
    result = exercise_1()
    cook_book = result[0]
    dish_persons_count = result[1]

    new_cook_book = {}  # Кукбук с количеством ингредиентов для одного человека

    for cook, ingredients in cook_book.items():
        for dish, cook_book_person_count in dish_persons_count.items():
            if cook == dish:
                new_cook_book[dish] = []
                for ingredient in ingredients:
                    new_ingredient = {'ingredient_name': ingredient['ingredient_name'],
                                      'quantity': float(ingredient['quantity']) / int(cook_book_person_count),
                                      'measure': ingredient['measure']}
                    new_cook_book[dish].append(new_ingredient)

    out_dict = {}

    for dish in dishes:
        try:
            for ingredient in new_cook_book[dish]:
                name = ingredient['ingredient_name']

                if name not in out_dict:
                    quantity = float(ingredient['quantity']) * int(person_count)
                    out_dict[name] = {'measure': ingredient['measure'],
                                      'quantity': quantity}
                else:
                    quantity = out_dict[name]['quantity'] + (ingredient['quantity'] * int(person_count))
                    out_dict[name] = {'measure': ingredient['measure'],
                                      'quantity': quantity}

        except KeyError:
            print(f'\nБлюда {dish} не найдено.\n')
    return out_dict


def show_result_1():
    result = exercise_1()
    cook_book = result[0]

    for cook, ingredients in cook_book.items():
        print(cook)
        for ingredient in ingredients:
            print(ingredient)
        print('\n' + '*' * 3 + '\n')

def show_result_2():
    result = get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Запеченный картофель'], 1)
    for item, props in result.items():
        print(item)
        print(props)



#show_result_1()  # Раскомментируйте, чтобы вывести результат

show_result_2()