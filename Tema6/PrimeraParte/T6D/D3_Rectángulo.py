class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__x2 > self.__x1 and self.__y2 > self.__y1:
            print("Error al establecer los valores")

    # Setters

    def set_x1(self, x1):
        if self.__x2 > self.__x1:
            print("Error al establecer los valores")
            self.__x1 = self.__x1
        else:
            self.__x1 = x1

    def set_y1(self, y1):
        if self.__y2 > self.__y1:
            print("Error al establecer los valores")
            self.__y1 = self.__y1
        else:
            self.__y1 = y1

    def set_x2(self, x2):
        if self.__x2 < self.__x1:
            print("Error al establecer los valores")
            self.__x2 = self.__x2
        else:
            self.__x2 = x2

    def set_y2(self, y2):
        if self.__y2 < self.__y1:
            print("Error al establecer los valores")
            self.__y2 = self.__y2
        else:
            self.__y2 = y2

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
        if self.__x2 > self.__x1:
            print("Error al establecer los valores")
            self.__x1 = self.__x1
        else:
            self.__x1 = x1

        if self.__y2 > self.__y1:
            print("Error al establecer los valores")
            self.__y1 = self.__y1
        else:
            self.__y1 = y1

    def set_x2_y2(self, x2, y2):
        if self.__x2 < self.__x1:
            print("Error al establecer los valores")
            self.__x2 = self.__x2
        else:
            self.__x2 = x2

        if self.__y2 < self.__y1:
            print("Error al establecer los valores")
            self.__y2 = self.__y2
        else:
            self.__y2 = y2

    def set_all(self, x1, y1, x2, y2):
        if self.__x2 > self.__x1:
            print("Error al establecer los valores")
            self.__x1 = self.__x1
        else:
            self.__x1 = x1

        if self.__y2 > self.__y1:
            print("Error al establecer los valores")
            self.__y1 = self.__y1
        else:
            self.__y1 = y1

        if self.__x2 < self.__x1:
            print("Error al establecer los valores")
            self.__x2 = self.__x2
        else:
            self.__x2 = x2

        if self.__y2 < self.__y1:
            print("Error al establecer los valores")
            self.__y2 = self.__y2
        else:
            self.__y2 = y2

    # Métodos

    def area(self):
        lado = (self.get_x2() - self.get_x1())
        altura = (self.get_y2() - self.get_y1())
        return lado * altura

    def perimetro(self):
        lado = (self.get_x2() - self.get_x1())
        altura = (self.get_y2() - self.get_y1())
        return lado * 2 + altura * 2

    def imprimir(self):
        print("Perímetro:", self.perimetro, "area:", self.area)


def main():
    rectangulo1 = Rectangulo(0, 0, 5, 5)
    rectangulo2 = Rectangulo(7, 9, 2, 3)

    rectangulo1.imprimir()
    rectangulo2.imprimir()

    print("Parte 2")

    rectangulo1.set_x1_y1(8, 10)
    rectangulo1.set_x2_y2(9, 6)

    rectangulo2.set_all(1, 2, 3, 4)

    rectangulo1.imprimir()
    rectangulo2.imprimir()


if __name__ == "__main__":
    main()
