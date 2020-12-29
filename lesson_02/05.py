from common import input_value

task = '''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

if __name__ == '__main__':
    print(task)

    raiting = [7, 5, 3, 3, 2]

    while True:
        raiting.sort(reverse = True)
        print('Raiting = ', raiting)
        num = input_value('Input number or 0 - to exit: ', '^[0-9]+$', int)
        if num == 0:
            break
        raiting.append(num)
