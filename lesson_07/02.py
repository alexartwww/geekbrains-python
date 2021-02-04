task = '''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''


class Clothes:
    @property
    def need_material(self):
        raise NotImplementedError("Необходимо переопределить метод")


class Costume(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def need_material(self):
        return (self.v / 6.5 + 0.5)


class Coat(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def need_material(self):
        return (2 * self.h + 0.3)


if __name__ == '__main__':
    print(task)

    objects = [
        231,
        22,
        Coat(32),
        'test',
        True,
        Costume(87),
        Coat(32)
    ]

    need_material = 0
    for obj in objects:
        if isinstance(obj, Clothes):
            need_material += obj.need_material

    print(need_material)