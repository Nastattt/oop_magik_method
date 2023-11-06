# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print('method new')
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p = Point(2, 8)
# print(p.x)

#
# class DataBase:
#     __instance = None
#
#     def __new__(cls,*args,**kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def __del__(self):
#         print('ksns')
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'cоединение с БД:{self.user},{self.password},{self.port}')
#
#     def close(self):
#         print('соединение разорвано')
#
#     def read(self):
#         print('чтение данных')
#
#     def write(self, data):
#         print(f'Записываем данные {data}')
#
#
# bd = DataBase('user', 'psw1', '8000')
# bd2 = DataBase('user', 'psw1', '8000')
# print(bd)
# print(bd2)
#
#
# class Test:
#
#     def __repr__(self):
#         return 'Object Test'
#
#     def __str__(self):
#         return 'Test String'
#
#     def __bool__(self):
#         return 2 < 6
#
# t = Test()
# if t:
#     print('kdcdinvvmmd')

class Clock:
    __Day = 86400

    def __init__(self,seconds:int):
        if not isinstance(seconds,int):
            raise TypeError('Нужео ввести челое число')
        self.seconds = seconds % self.__Day

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h}:{m}:{s}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.seconds == other
        elif isinstance(other, Clock):
            return self.seconds == other.seconds
        else:
            raise TypeError('Нужно ввести целое число или экземпляр класса Clock')

    def __lt__(self, other):
        if not isinstance(other(int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __ls__(self, other):
        if not isinstance(other(int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

    def __add__(self,other):
        if not isinstance(other,(int,Clock)):
            raise TypeError('Не можем сложить')

        sc = other if isinstance(other,int) else other.seconds
        return Clock(self.seconds + sc)


cl = Clock(86400)
cl2 = Clock(54)
cl = cl + 20
print(cl.get_time())
cl = cl + cl2
print(cl.get_time())





