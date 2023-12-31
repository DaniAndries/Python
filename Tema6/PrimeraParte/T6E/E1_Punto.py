import math
import random


class Punto:
    def __init__(self, x=random.randint(-100, 100), y=random.randint(-100, 100)):
        self.__x = x
        self.__y = y

    # Setters
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    # Getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x_y(self, x, y):
        self.__x = x
        self.__y = y

    # Funciones

    def desplaza(self, dx, dy):
        if dx < 0:
            self.__x -= dx
        else:
            self.__x += dx
        if dy < 0:
            self.__x -= dy
        else:
            self.__x += dy

    def distancia(self, p):
        return abs(math.pow((p.x - self.__x), 2) + math.pow((p.y - self.__y), 2))

    def imprimir(self):
        print("Coordenada x:", self.get_x(), "Coordenada y:", self.get_y())


def main():
    punto1 = Punto(5, 0)
    punto2 = Punto(10, 10)
    punto3 = Punto(-3, 7)
    punto4 = Punto()

    punto1.imprimir()
    punto2.imprimir()
    punto3.imprimir()
    punto4.imprimir()

    print("Segunda Parte")

    punto1.set_x(5)
    punto1.set_y(10)
    punto2.set_x(3)
    punto2.set_y(9)
    punto3.set_x(6)
    punto3.set_y(15)

    punto1.imprimir()
    punto2.imprimir()
    punto3.imprimir()
    punto4.imprimir()


if __name__ == "__main__":
    main()
