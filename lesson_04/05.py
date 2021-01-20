from functools import reduce

task = '''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

if __name__ == '__main__':
    print(task)

    result = reduce(lambda x, y: x*y, [i for i in range(100, 1001, 2)])
    print(result)