documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Покемон Аристархович"},
    {"type": "passport", "number": "777994", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "95425", "name": "Федор Емельяненко"},
    {"type": "insurance", "number": "946732345"},
    {"type": "invoice", "number": "1247", "name": "Шушлай Козловский"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006', '1247'],
    '3': ['777994', '95425', '946732345']
}


def check_docs(data):  # Для задания 3 по исключениям.
    temp_documents = []
    print('Все документы:')
    print('*' * 30)
    for doc in data:
        try:
            print('Имя владельца:', doc['name']+'.', '\nНомер документа: ', doc['number']+'.', '\nТип документа: ',
                  doc['type'])
            print('*'*30)
        except KeyError:
            doc['name'] = 'У документа отсутсвует владелец'
            print('Имя владельца:', doc['name'] + '.', '\nНомер документа: ', doc['number'] + '.', '\nТип документа: ',
                  doc['type'])
            print('*' * 30)
        finally:
            temp_documents.append(doc)
    return temp_documents

documents = check_docs(documents)


def get_name(document):
    print('Введите номер документа, например: 10006')
    doc_num = input()

    for number in document:
        if number['number'] == doc_num:
            return number['name']
        else:
            continue
    return False


def get_docs(document):
    docs_list = ''
    for item in document:
        docs_list += item['type'] + ' "' + item['number'] + '" ' + '"' + item['name'] + '"\n'
    return docs_list


def get_shelf_number(doc_num, directory):
    for shelf in directory:
        if doc_num in directory[shelf]:
            return shelf
        else:
            continue
    return False


def add_doc(document, directory):
    print('\nДля добавления нового документа введите следующую информацию:')
    print('Тип документа:')
    doc_type = input()
    print('Номер документа:')
    doc_num = input()
    print('Имя владельца:')
    doc_name = input()
    all_shelfs = '\n'
    for key in directory.keys():
        all_shelfs += key + '\n'
    print('\nУкажите номер полки, на которой будет храниться документ: {}'.format(all_shelfs))
    doc_shelf = input()

    def check_shelf(doc_shelf):
        if doc_shelf in directory.keys():
            return True
        else:
            return False

    new_doc = {"type": doc_type, "number": doc_num, "name": doc_name}

    if check_shelf(doc_shelf):
        document.append(new_doc)
        directory[doc_shelf].append(new_doc['number'])
        return document, directory
    else:
        print('\nТакой полки не существует!\n')
        return False


################################################################################
################################################################################
################################################################################
def del_doc(document, directory):
    print('Введите номер документа для удаления:')
    input_num = input()
    doc_num = ''
    result = []

    for shelf, numbers in directory.items():
        if input_num in numbers:
            doc_num = input_num
            del (directory[shelf][numbers.index(doc_num)])
            result.append(directory)
            break
        else:
            continue

    if doc_num == input_num:
        for doc in document:
            if doc['number'] == doc_num:
                del [document[document.index(doc)]]
                break
            else:
                continue

        result.append(document)
        return result
    else:
        return False


def move_doc(directory):
    print('Введите номер документа.')
    doc_num = input()
    for shelf, documents in directory.items():
        if doc_num not in documents:
            continue
        else:
            print(directory)
            doc = directory[shelf].index(doc_num)
            doc = directory[shelf].pop(doc)
            print('Введите номер полки, на которую необходимо переместить документ.')
            shelf_num = input()
            if shelf_num not in directory:
                return False
            else:
                directory[shelf_num].append(doc)
                print(directory)
                return directory
    return False


def new_shelf(directory):
    print('Введите номер новой полки:')
    input_shelf = input()
    if input_shelf in directory:
        print('Такой номер уже существует.')
        new_shelf(directory)
    else:
        directory[input_shelf] = []
        return directory


################################################################################
################################################################################
################################################################################
def run(document=documents, directory=directories, program=True):
    while program == True:
        print('Введите команду:')
        print('p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
        print('l – команда, которая выведет список всех документов')
        print('s – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
        print(
            'a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться')
        print('d – команда, которая спросит номер документа и удалит его из каталога и из перечня полок')
        print(
            'm - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую')
        print('as - команда, которая спросит номер новой полки и добавит ее в перечень')

        print('\n\nq - выйти из программы.')

        command = input()
        if command == 'p':
            result = get_name(document)

            if result != 0:
                print('Товарищ найден: {}\n'.format(result))
            else:
                print('Товарища с таким номером не найдено.\n')

        elif command == 'l':
            print(get_docs(document))

        elif command == 's':
            print('Введите номер документа, например: 10006')
            doc_num = input()
            result = get_shelf_number(doc_num, directory)
            if result != 0:
                print('Документ найден на полке: {}\n'.format(result))
            else:
                print('Документ не найден.\n')

        elif command == 'a':
            result = add_doc(document, directory)
            if result != 0:
                documents = result[0]
                directories = result[1]
                print('Документ успешно добавлен!\n')
            else:
                print('Что-то пошло не так :(')

        elif command == 'd':
            result = del_doc(document, directory)
            if result != 0:
                documents = result[0]
                directories = result[1]
                print('\nУспешно удалено!\n')
            else:
                print('Что-то пошло не так :(\n')

        elif command == 'm':
            result = move_doc(directory)
            if result != 0:
                directories = result
                print('\nУспешно перемещено!\n')
            else:
                print('Что-то пошло не так :(\n')

        elif command == 'as':
            result = new_shelf(directory)
            directories = result
            print('\nУспешно добавлено!\n')

        elif command == 'q':
            program = False
    return


run()