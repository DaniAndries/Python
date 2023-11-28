import random


class Rectangulo:
    __MIN = 0
    __MAX = 100

    def __init__(self, x1=random.randint(__MIN, __MAX), y1=random.randint(__MIN, __MAX),
                 x2=random.randint(__MIN, __MAX), y2=random.randint(__MIN, __MAX)):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__x2 > self.__x1 and self.__y2 > self.__y1:
            print("Error al establecer los valores")

    # Setters

    def set_x1(self, x1):
        if Rectangulo.__MIN <= x1 <= Rectangulo.__MAX and self.__x2 < self.__x1 and self.__y2 < self.__y1:
            self.__x1 = x1
        else:
            print("Error al establecer los valores")

    def set_y1(self, y1):
        if Rectangulo.__MIN <= y1 <= Rectangulo.__MAX and self.__x2 < self.__x1 and self.__y2 < self.__y1:
            self.__y1 = y1
        else:
            print("Error al establecer los valores")

    def set_x2(self, x2):
        if Rectangulo.__MIN <= x2 <= Rectangulo.__MAX and self.__x2 < self.__x1 and self.__y2 < self.__y1:
            self.__x2 = x2
        else:
            print("Error al establecer los valores")

    def set_y2(self, y2):
        if Rectangulo.__MIN <= y2 <= Rectangulo.__MAX and self.__x2 < self.__x1 and self.__y2 < self.__y1:
            self.__y2 = y2
        else:
            print("Error al establecer los valores")

    # Getters
    def get_x1(self):
        return self.__x1

    def get_y1(self):
        return self.__y1

    def get_x2(self):
        return self.__x2

    def get_y2(self):
        return self.__y2

    def set_x1_y1(self, x1, y1):
        if Rectangulo.__MIN <= x1 <= Rectangulo.__MAX and x1 < self.__x2 and y1 < self.__y2:
            self.__x1 = x1
            self.__y1 = y1

        else:
            print("Error al establecer los valores")

    def set_x2_y2(self, x2, y2):
        if Rectangulo.__MIN <= x2 <= Rectangulo.__MAX and self.__x1 < x2 and self.__y1 < y2:
            self.__x2 = x2
            self.__y2 = y2
        else:
            print("Error al establecer los valores")

    def set_all(self, x1, y1, x2, y2):
        if Rectangulo.__MIN <= x1 <= Rectangulo.__MAX and x1 < self.__x2 and y1 < self.__y2:
            self.__x1 = x1
            self.__y1 = y1

        else:
            print("Error al establecer los valores")

        if Rectangulo.__MIN <= x2 <= Rectangulo.__MAX and self.__x1 < x2 and self.__y1 < y2:
            self.__x2 = x2
            self.__y2 = y2
        else:
            print("Error al establecer los valores")

    # Métodos

    def area(self):
        return (self.__x2 - self.__x1) * (self.__y2 - self.__y1)

    def perimetro(self):
        return (self.__x2 - self.__x1) * 2 + (self.__y2 - self.__y1) * 2

    def imprimir(self):
        print("Perímetro:", self.perimetro(), "area:", self.area())


def main():
    rectangulo1 = Rectangulo(0, 0, 5, 5)
    rectangulo2 = Rectangulo(7, 9, 2, 3)
    rectangulo3 = Rectangulo()

    rectangulo1.imprimir()
    rectangulo2.imprimir()
    rectangulo3.imprimir()

    print("Parte 2")

    rectangulo1.set_x1_y1(8, 10)
    rectangulo1.set_x2_y2(9, 6)

    rectangulo2.set_all(1, 2, 3, 4)

    rectangulo1.imprimir()
    rectangulo2.imprimir()


if __name__ == "__main__":
    main()
