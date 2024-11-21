import math

class Figure:
    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        self.sides_count = len(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, (int, float)) and side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def is_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        self.__circumference = circumference
        self.__radius = self.__calculate_radius(circumference)
        super().__init__([circumference], color, True)

    def __calculate_radius(self, circumference):
        return circumference / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, new_circumference):
        if isinstance(new_circumference, (int, float)) and new_circumference > 0:
            self.__circumference = new_circumference
            self.__radius = self.__calculate_radius(new_circumference)
            super().set_sides(new_circumference)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)

    def get_square(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled):
        sides = [side_length] * self.sides_count
        super().__init__(sides, color, filled)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6, True)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
