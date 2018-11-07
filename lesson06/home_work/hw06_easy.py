# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = {'a': [x1, y1],
                       'b': [x2, y2],
                       'c': [x3, y3]
                       }
        self.sides = [self.side_len(self.points['a'], self.points['b']),
                      self.side_len(self.points['b'], self.points['c']),
                      self.side_len(self.points['c'], self.points['a'])]

    @staticmethod
    def side_len(pnt1, pnt2):
        x = 0
        y = 1
        return round(((pnt2[x]-pnt1[x])**2+(pnt2[y]-pnt1[y])**2)**0.5,2)

    def perimeter(self):
        return round(sum(self.sides),2)

    def height(self):
        base_len = max(self.sides)
        base_side = self.sides.index(base_len)
        other_sides = self.sides.copy()
        other_sides.pop(base_side)
        if sum(other_sides)>base_side:
            p = self.perimeter()/2
            h = round((2/base_len)*((p * (p - other_sides[0]) * (p - other_sides[1]) * (p - base_len))**0.5),2)
            return h

    def square(self):

        h = self.height()
        if h:
            s = round(0.5 * h * max(self.sides),2)
            return s


triangle1 = Triangle(2,1,-2,-2,-4,3)

print(f'Длины сторон треугольника {triangle1.sides}')
print(f'Периметр треугольника равен {triangle1.perimeter()}')
print(f'Высота треугольника к основанию равна {triangle1.height()}')
print(f'Площадь треугольника равна {triangle1.square()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class EqualSidedTrap:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.points = {'a': [x1, y1],
                       'b': [x2, y2],
                       'c': [x3, y3],
                       'd': [x4, y4],
                       }
        self.sides = self.sides_len()

    @staticmethod
    def side_len(pnt1, pnt2):
        x = 0
        y = 1
        return round(((pnt2[x] - pnt1[x]) ** 2 + (pnt2[y] - pnt1[y]) ** 2) ** 0.5, 2)

    def sides_len(self):
        sides = [self.side_len(self.points['a'], self.points['b']),
                 self.side_len(self.points['b'], self.points['c']),
                 self.side_len(self.points['c'], self.points['d']),
                 self.side_len(self.points['d'], self.points['a'])
                 ]

        return sides

        x = 0
        y = 1

        if (sides[0] == sides[2] and
            self.points['a'][y] == self.points['d'][y] and
            self.points['c'][y] == self.points['b'][y]) or \
            (sides[1] == sides[3] and
             self.points['a'][x] == self.points['b'][x] and
             self.points['c'][x] == self.points['d'][x]):
            return round(sides, 2)
        else:
            print('Фигура не является равнобедренной трапецией')

    def perimeter(self):
        if self.sides:
            return round(sum(self.sides), 2)

    def square(self):

        if self.sides:

            x = 0
            y = 1

            if self.sides[0] == self.sides[2]:
                return (self.sides[1]+self.sides[3])/2 * (self.points['b'][y] - self.points['a'][y])

            elif self.sides[1] == self.sides[3]:
                return round((self.sides[0] + self.sides[2]) / 2 * (self.points['d'][x] - self.points['a'][x]), 2)

equal_trap = EqualSidedTrap(-2,2,2,2,4,-2,-4,-2)

print(f'Длины сторон трапеции {equal_trap.sides}')
print(f'Периметр трапеции равен {equal_trap.perimeter()}')
print(f'Площадь трапции равна {equal_trap.square()}')

