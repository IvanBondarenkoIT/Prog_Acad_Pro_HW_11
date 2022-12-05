from datetime import datetime


# 1) Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.
class MyDescriptor:
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        # print(self)
        # print(instance_self)
        # print(instance_class)
        return self.n * instance_self.p

    def __set__(self, instance_self, value):
        # print("Read only!")
        return NotImplementedError("Read only!")


class Box:
    def __init__(self, x, y, z):
        self.p = x*y*z
    volume = MyDescriptor(2)


# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.
class Circle:
    LOG_TXT_FILE = "txt.txt"

    def __init__(self, x, y, radius=1):
        self.x = x
        self.y = y
        self.__radius = radius  # HW_11.3

    def __setattr__(self, key, value):
        if isinstance(value, int):
            return object.__setattr__(self, key, value)
        else:
            raise NotImplementedError("Not integer")

    # 3) Реализуйте свойство класса, которое обладает следующим функционалом:
    # при установки значения этого свойства в файл с заранее
    # определенным названием должно сохранятся время (когда устанавливали
    # значение свойства) и установленное значение.

    def log_to_file(self, value):
        with open(self.LOG_TXT_FILE, "a") as file:
            file.write(f"radius - {value} : {datetime.now()}\n")

    @property
    def radius(self):
        print(1)
        return self.__radius

    @radius.setter
    def radius(self, radius):
        print(2)
        self.log_to_file(radius)
        self.__radius = radius


def main():
    # HW_11.1
    b1 = Box(1, 2, 3)
    print(b1.volume)
    b1.volume = 15
    print(b1.volume)
    # HW_11.2
    p1 = Circle(10, 12)
    print(f"cords({p1.x},{p1.y})")
    try:
        p1.x = "20"
        p1.y = 24
    except Exception as ex:
        print(ex)
    print(f"cords({p1.x},{p1.y})")
    # HW_11.3
    print(p1.radius)
    p1.radius = 5
    p1.radius = 10
    print(p1.radius)


if __name__ == "__main__":
    main()
