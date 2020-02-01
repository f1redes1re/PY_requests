from contextlib import contextmanager
import datetime
from sys import exc_info

@contextmanager
def loger(path):
    try:
        file = open(path, 'a', encoding='utf8')
        a = datetime.datetime.now()
        file.write(f'Приводится время лога запуска: {a}\n')
        yield file
    finally:
        exc_type, exc_val, exc_tb = exc_info()
        b = datetime.datetime.now()
        file.write(f'{b}\n')
        print(f'Разница времени между запуском и выходом из программы: {b - a}')
        file.close()


if __name__ == '__main__':
    with loger(path='log2.txt') as log:
        log.write('Приводится время лога выхода: ')


        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

        # p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
        def p_people(some_param):
            number_counter = 0
            sum_input = input('Введите номер документа: ')
            for sum2 in some_param:
                if sum2["number"] != sum_input:
                    number_counter += 1
                if number_counter % len(sum2) == 0:
                    print('Такого документа нет в списке документов')
                else:
                    if sum2["number"] == sum_input:
                        print(sum2["name"])

        # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        def l_list(some_param):
            for documents1 in some_param:
                print('{} {} {}'.format(documents1["type"], '"' + documents1["number"] + '"',
                                        '"' + documents1["name"] + '"'))

        # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        def s_shelf(some_param):
            number_input = input('Введите номер документа: ')
            for doc_num in some_param:
                if number_input in some_param[doc_num]:
                    print("Документ находится на полке № {}".format(doc_num))
                    return
            print('Такого документа нет на полках с документами')

        # a – add – команда, которая добавит новый документ в каталог и в перечень полок,
        # спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
        def a_add(some_param, some_param_1):
            doc_type = input('Введите тип документа: ')
            doc_num = input('Введите номер документа: ')
            person_name = input('Введите имя человека: ')
            shelf_num = input('Введите номер полки: ')
            documents_add = {"type": doc_type, "number": doc_num, "name": person_name}
            some_param.append(documents_add)
            if shelf_num in some_param_1.keys():
                some_param_1[shelf_num].append(doc_num)
            else:
                some_param_1.setdefault(shelf_num, [doc_num])
            print(f'{some_param} \n{some_param_1}')
            return

        # Задача №2. Дополнительная (не обязательная)
        # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
        def d_delete(some_param, some_param_1):
            doc_num_input = input('Введите номер документа: ')
            for doc_num_1 in some_param_1.values():
                if doc_num_input in doc_num_1:
                    doc_num_1.remove(doc_num_input)
                    for doc_num_1 in some_param:
                        if doc_num_input in doc_num_1["number"]:
                            some_param.remove(doc_num_1)
                            print(f'{documents} \n{directories}')
                            return
            print('Такого документа нет на полках с документами')

        # m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
        def m_move(some_param):
            doc_num_input = input('Введите номер документа: ')
            shelf_num_input = input('На какую полку положить документ: ')
            for shelf_num in some_param.keys():
                if shelf_num_input in shelf_num:
                    for doc_num_1 in some_param.values():
                        if doc_num_input in doc_num_1:
                            doc_num_1.remove(doc_num_input)
                            some_param[shelf_num_input].append(doc_num_input)
                            print(some_param)
                            return
                    print('Такого документа нет на полках с документами')
                    return
            print('Такой полки нет!')
            return

        # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
        def add_shelf(some_param):
            new_shelf = input('Введите номер новой полки: ')
            some_param.setdefault(new_shelf, [])
            print(some_param)

        # Меню запуска функций
        def menu():
            user_input = input('Введите нужную команду: ')
            if user_input == 'p':
                p_people(documents)
                return
            elif user_input == 'l':
                l_list(documents)
                return
            elif user_input == 's':
                s_shelf(directories)
                return
            elif user_input == 'a':
                a_add(documents, directories)
                return
            elif user_input == 'd':
                d_delete(documents, directories)
                return
            elif user_input == 'm':
                m_move(directories)
                return
            elif user_input == 'as':
                add_shelf(directories)
                return
            elif user_input == 'quit':
                print('Конец программы')
                return

        menu()
