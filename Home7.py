"1.	Создай класс Circle с protected атрибутом _radius. Добавь @property для radius (с проверкой: радиус > 0), "
"и вычисляемые свойства area и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса."

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius   # используем setter для проверки

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

c = Circle(10)
print(c.radius)      # 10
print(c.area)        # 314.159...
print(c.perimeter)   # 62.831...
c.radius = 5         # автоматически пересчитает площадь и периметр
print(c.area)        # 78.539...
print(c.perimeter)   # 31.415...

". Создай класс Vector с атрибутами x и y. Реализуй магические методы __add__ (сложение двух векторов), __str__ "
"(вывод в формате class Vector(x, y)",
"и __eq__ (сравнение). Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6)."

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)          # Vector(4, 6)

print(v3 == Vector(4, 6))   # True

"3.	Создай класс Temperature с @property для celsius, fahrenheit и kelvin. "
"При установке значения через любое свойство должны автоматически пересчитываться остальные."
" Хранить следует только одно внутреннее значение."

class Temperature:
    def __init__(self, celsius):
        self._celsius = float(celsius)   # внутреннее единственное значение

    # --- Celsius ---
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = float(value)

    # --- Fahrenheit ---
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (float(value) - 32) * 5/9

    # --- Kelvin ---
    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = float(value) - 273.15

t = Temperature(0)

print(t.celsius)      # 0.0
print(t.fahrenheit)   # 32.0
print(t.kelvin)       # 273.15

t.fahrenheit = 212    # кипение воды
print(t.celsius)      # 100.0
print(t.kelvin)       # 373.15

t.kelvin = 0          # абсолютный ноль
print(t.celsius)      # -273.15
print(t.fahrenheit)   # -459.67

"Используй @dataclass для создания класса Point с полями x: float и y: float. "
"Добавь метод distance_to(other: Point) - расстояние до другой точки. "
"Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to."

from dataclasses import dataclass
import math

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: "Point3D") -> float:
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2 +
            (self.z - other.z)**2
        )
p1 = Point(0, 0)
p2 = Point(3, 4)

print(p1.distance_to(p2))   # 5.0

a = Point3D(0, 0, 0)
b = Point3D(1, 2, 2)

print(a.distance_to(b))     # 3.0


". Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. Реализуй __iter__ и __next__ "
"(при исчерпании бросай StopIteration). Проверь в цикле for и через list()."

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)

5
4
3
2
1
0
