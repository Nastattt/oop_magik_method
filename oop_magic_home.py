# # class Passport:
# #     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.date_of_birth = date_of_birth
# #         self.country = country
# #         self.numb_of_pasport = numb_of_pasport
# #
# #     def PrintInfo(self):
# #         print(f'''
# # Full name: {self.first_name} {self.last_name}
# # Date of Birth: {self.date_of_birth}
# # Country: {self.country}
# # Passport: {self.numb_of_pasport}
# # ''')
# #
# #     def __repr__(self):
# #         return f'name {self.first_name} {self.last_name}, Passport {self.numb_of_pasport}'
# #
# #
# # class ForeIgnPassport(Passport):
# #
# #     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport, visa):
# #         super().__init__(first_name, last_name, country, date_of_birth, numb_of_pasport)
# #         self.visa = visa
# #
# #     def PrintInfo(self):
# #         super().PrintInfo()
# #         print('Visa:', self.visa)
# #
# # MFC = []
# # p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 457896')
# # MFC.append(p)
# # fp = ForeIgnPassport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 457896', 'China')
# # MFC.append(fp)
# # print(MFC)
# # for item in MFC:
# #     item.PrintInfo()
# #
# # my_str = 'fhbvhsfvfsbhb'
# # my_list = [1, 5, 4, 3, 55, 3, 44, 2, 2]
# #
# # for char in my_str:
# #     print(char)
# #
# # for number in my_list:
# #     print(number)
#
# #
# # class Equipment:
# #
# #     def init(self, name, make, year):
# #         self.name = name
# #         self.make = make
# #         self.year = year
# #
# #     def action(self):
# #         return 'не определено'
# #
# #     def __str__(self):
# #         return f'{self.name}, {self.make}, {self.year}.'
# #
# #     def __le__(self, other):
# #         if not isinstance(other,Equipment):
# #             raise TypeError
# #         return self.year <= other.year
# #
# #
# # class Printer(Equipment):
# #
# #     def init(self, series, name, make, year):
# #         super().init(name, make, year)
# #         self.series = series
# #
# #     def action(self):
# #         return 'печатает'
# #
# #     def str(self):
# #         return f'{self.series}, {self.name}, {self.make}, {self.year}'
# #
# # def allItemes(sklad):
# #     for item in sklad:
# #         print(item)
# #
# # class Scaner(Equipment):
# #
# #     def init(self, name, make, year):
# #         super().init(name, make, year)
# #
# #     def action(self):
# #         return 'сканирует'
# #
# #
# # class Xerox(Equipment):
# #     def init(self, name, make, year):
# #         super().init(name, make, year)
# #
# #     def action(self):
# #         return 'копирует и печатает на листочек'
# #
# # def get_items(skad):
# #     for item in sklad:
# #         if isinstance(item, Printer):
# #             print(item)
# #
# # sklad =[]
# # e = Equipment('Noname','X',200)
# # sklad.append(e)
# # s = Printer('fhjvbeivb','jfhv','jdvnb',2545)
# # x = Xerox('nbjfnb','ifjhurh',5000)
# #
#
#
# # #Битва
# # from random import randint
# #
# # class Soldier:
# #     def __init__(self, name='Noname', health=100):
# #         self.name = name
# #         self.health = health
# #
# #     def set_name(self, name):
# #         self.name = name
# #
# #     def make_kick(self, enemy):
# #         enemy.health -= 20
# #         if enemy.health < 0:
# #             enemy.health = 0
# #         self.health += 10
# #         print(self.name, "бьет", enemy.name)
# #         print(f'{enemy.name} = {enemy.health}')
# #
# #     def __str__(self):
# #         return f"{self.name} (Health: {self.health})"
# #
# #     def __lt__(self, other):
# #         return self.health < other.health
# #
# # class Battle:
# #     def __init__(self, u1, u2):
# #         self.u1 = u1
# #         self.u2 = u2
# #         self.result = "Сражения не было"
# #
# #     def battle(self):
# #         while self.u1.health > 0 and self.u2.health > 0:
# #             n = randint(1, 2)
# #             if n == 1:
# #                 self.u1.make_kick(self.u2)
# #             else:
# #                 self.u2.make_kick(self.u1)
# #
# #         if self.u1.health > self.u2.health:
# #             self.result = f"{self.u1.name} ПОБЕДИЛ"
# #         elif self.u2.health > self.u1.health:
# #             self.result = f"{self.u2.name} ПОБЕДИЛ"
# #
# #     def who_win(self):
# #         return self.result
# #
# # first = Soldier('Mr. First', 140)
# # second = Soldier()
# # second.set_name('Mr. Second')
# # b = Battle(first, second)
# # b.battle()
# # print(b.who_win())
# #
# #
# # import time
# # import random
# #
# # # Класс Card представляет отдельную карту
# # class Card:
# #     # Статические списки для значений мастей и номеров карт
# #     NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
# #     MastList = ["пик", "крестей", "бубей", "червей"]
# #
# #     # Конструктор класса Card
# #     def __init__(self, i, j):
# #         # Инициализация атрибутов масти и номера из списков
# #         self.Mastb = self.MastList[i - 1]  # Выбираем масть карты
# #         self.Num = self.NumsList[j - 1]  # Выбираем номер карты
# #
# # # Класс DeckOfCards представляет колоду карт
# # class DeckOfCards:
# #     # Конструктор класса DeckOfCards
# #     def __init__(self):
# #         # Инициализация атрибута deck как списка из 56 элементов
# #         self.deck = [None] * 56  # 56 карт в колоде
# #         k = 0  # Переменная для отслеживания позиции в колоде
# #         for i in range(1, 4 + 1):  # Цикл по мастям
# #             for j in range(1, 14 + 1):  # Цикл по номерам
# #                 # Создание новой карты и добавление ее в колоду
# #                 self.deck[k] = Card(i, j)
# #                 k += 1
# #
# #     # Метод для перемешивания карт в колоде
# #     def shuffle(self):
# #         random.shuffle(self.deck)  # Случайное перемешивание колоды
# #
# #     # Метод для получения информации о карте по индексу
# #     def get(self, i):
# #         if 0 <= i <= 55:  # Проверка, что индекс находится в допустимом диапазоне
# #             answer = self.deck[i].Num  # Получаем номер карты
# #             answer += " "
# #             answer += self.deck[i].Mastb  # Получаем масть карты
# #         else:
# #             answer = "В колоде только 56 карт"  # Сообщение об ошибке, если индекс недопустим
# #         return answer
# #
# # # Создание объекта класса DeckOfCards
# # deck = DeckOfCards()  # Создали колоду
# # deck.shuffle()  # Перемешали колоду
# #
# # # Пользовательский ввод номера карты
# # print('Выберите карту из колоды в 56 карт:')
# # n = int(input())
# # if n <= 56:
# #     card = deck.get(n - 1)  # Получение информации о выбранной карте
# #     print('Вы взяли карту: ', card, end='.\n')  # Вывод информации о карте
# # else:
# #     print("В колоде только 56 карт")  # Вывод сообщения об ошибке, если номер карты недопустим
#
#
#
#
# # Вектор
# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def display(self):
#         print(f"({self.x}, {self.y}, {self.z})")
#
#     def read(self):
#         self.x = int(input("Enter x: "))
#         self.y = int(input("Enter y: "))
#         self.z = int(input("Enter z: "))
#
#     def __add__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#         else:
#             raise ValueError("Can only add another Vector3D object")
#
#     def __sub__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#         else:
#             raise ValueError("Can only subtract another Vector3D object")
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#         elif isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         else:
#             raise ValueError("Multiplication not supported for this data type")
#
#     def __matmul__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(
#                 self.y * other.z - self.z * other.y,
#                 self.z * other.x - self.x * other.z,
#                 self.x * other.y - self.y * other.x
#             )
#         else:
#             raise ValueError("Can only compute the cross product with another Vector3D object")
#
#
# v1 = Vector3D(4, 1, 2)
# v1.display()
#
# v2 = Vector3D()
# v2.read()
#
# v3 = Vector3D(1, 2, 3)
#
# v4 = v1 + v2
# v4.display()
#
# a = v4 * v3
# print(a)
#
# v4 = v1 * 10
# v4.display()
#
# v4 = v1 @ v3
# v4.display()
#



# Треугольник
# import math
#
# class Triangle:
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#
#     def increase_side(self, percent):
#         self.side1 *= 1 + percent / 100
#         self.side2 *= 1 + percent / 100
#
#     def decrease_side(self, percent):
#         self.side1 *= 1 - percent / 100
#         self.side2 *= 1 - percent / 100
#
#     def radius_of_circumscribed_circle(self):
#         return (self.side1 * self.side2) / (2 * math.sqrt(self.side1**2 + self.side2**2))
#
#     def perimeter(self):
#         return self.side1 + self.side2 + math.sqrt(self.side1**2 + self.side2**2)
#
#     def angles(self):
#         angle1 = math.degrees(math.asin(self.side1 / self.perimeter()))
#         angle2 = math.degrees(math.asin(self.side2 / self.perimeter()))
#         angle3 = 180 - angle1 - angle2
#         return angle1, angle2, angle3
#
# # Пример использования:
# triangle = Triangle(3, 4)
# print("Исходные стороны:", triangle.side1, triangle.side2)
#
# triangle.increase_side(10)
# print("Строны после увеличения на 10%:", triangle.side1, triangle.side2)
#
# triangle.decrease_side(10)
# print("Строны после уменьшения на 10%:", triangle.side1, triangle.side2)
#
# print("Радиус описанной окружности:", triangle.radius_of_circumscribed_circle())
# print("Периметр треугольника:", triangle.perimeter())
# print("Значения углов:", triangle.angles())




# автобус
class Bus:
    def __init__(self):
        self.speed = 0
        self.capacity = 0
        self.maxSpeed = 100
        self.passengers = []
        self.seats = {}
        self.hasEmptySeats = False

    def boarding(self, passenger_names):
        for name in passenger_names:
            if len(self.passengers) < self.capacity:
                self.passengers.append(name)
                self.seats[name] = True
                print(f"{name} boarded the bus.")
            else:
                print(f"No empty seats for {name}.")

    def getOff(self, passenger_names):
        for name in passenger_names:
            if name in self.passengers:
                self.passengers.remove(name)
                self.seats[name] = False
                print(f"{name} got off the bus.")
            else:
                print(f"{name} is not on the bus.")

    def increaseSpeed(self, value):
        if self.speed + value <= self.maxSpeed:
            self.speed += value
            print(f"Speed increased to {self.speed} km/h.")
        else:
            print("Speed can't exceed the maximum speed.")

    def decreaseSpeed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Speed decreased to {self.speed} km/h.")
        else:
            print("Speed can't go below 0.")

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.boarding([passenger_name])
        return self

    def __isub__(self, passenger_name):
        self.getOff([passenger_name])
        return self

# Пример использования
bus = Bus()
bus.capacity = 30  # Устанавливаем максимальную вместимость
bus.boarding(["Alice", "Bob", "Charlie"])  # Посадка пассажиров
bus.increaseSpeed(10)  # Увеличение скорости
bus += "David"  # Посадка еще одного пассажира
bus -= "Alice"  # Высадка пассажира
if "Bob" in bus:  # Проверка наличия пассажира
    print("Bob is on the bus.")



