# Домашнее задание про исключения!

# Задачи 1 и 2


def polish_notation():
    operation = input('Введите сначала операцию, затем первое число, далее второе - все через пробел: ')
    operation_1, num1, num2 = operation.split()
    num1 = int(num1)
    num2 = int(num2)
    all_operations = ['+', '-', '*', '/']

    assert operation_1 in all_operations, 'Данной операции нет в списке доступных операций!'
    assert num1 >= 0 and num2 >= 0, 'Вводить можно только целые положительные числа!'

    if operation_1 == '+':
        result = num1 + num2
    elif operation_1 == '-':
        result = num1 - num2
    elif operation_1 == '*':
        result = num1 * num2
    elif operation_1 == '/':
        result = num1 / num2
    return result


try:
    print(polish_notation())
except AssertionError as e1:
    print(e1)
except ZeroDivisionError as e2:
    print(e2, 'Деление на ноль!')
except ValueError as e3:
    print(e3, 'Введены некорректные данные для заполнения!')
except KeyError as e4:
    print(e4, 'Несуществующий ключ!')
except SyntaxError as e5:
    print(e5, 'Синтаксическая ошибка!')
except TypeError as e6:
    print(e6, 'Операция применена к объекту несоответствующего типа!')
else:
    print('Все сработано верно, ура!')


# ИСКЛЮЧЕНИЯ - Задача №3
print('\n')
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "zzz", "number": "111"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


def all_name(some_param):
    for documents_name in some_param:
        try:
            print('{} {} {}'.format(documents_name["type"], documents_name["number"], documents_name["name"]))
        except KeyError:
            print('В документе с номером {} отсутствует поле "name"!'.format(documents_name["number"]))
all_name(documents)
