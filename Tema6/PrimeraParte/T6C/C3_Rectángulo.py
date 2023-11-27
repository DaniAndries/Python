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


def main():
    rectangulo1 = Rectangulo(0, 0, 5, 5)
    rectangulo2 = Rectangulo(7, 9, 2, 3)

    lados1 = (rectangulo1.get_x2() - rectangulo1.get_x1())
    alturas1 = (rectangulo1.get_y2() - rectangulo1.get_y1())
    perimetro1 = (lados1 * 2 + alturas1 * 2)
    area1 = (lados1 * alturas1)

    lados2 = (rectangulo2.get_x2() - rectangulo2.get_x1())
    alturas2 = (rectangulo2.get_y2() - rectangulo2.get_y1())
    perimetro2 = (lados2 * 2 + alturas2 * 2)
    area2 = (lados2 * alturas2)

    print("Perímetro:", perimetro1, "area:", area1)
    print("Perímetro:", perimetro2, "area:", area2)

    print("Parte 2")

    rectangulo1.set_x1(8)
    rectangulo1.set_y1(10)
    rectangulo1.set_x2(9)
    rectangulo1.set_y2(6)

    rectangulo2.set_x1(1)
    rectangulo2.set_y1(2)
    rectangulo2.set_x2(3)
    rectangulo2.set_y2(4)

    lados1 = (rectangulo1.get_x2() - rectangulo1.get_x1())
    alturas1 = (rectangulo1.get_y2() - rectangulo1.get_y1())
    perimetro1 = (lados1 * 2 + alturas1 * 2)
    area1 = (lados1 * alturas1)

    lados2 = (rectangulo2.get_x2() - rectangulo2.get_x1())
    alturas2 = (rectangulo2.get_y2() - rectangulo2.get_y1())
    perimetro2 = (lados2 * 2 + alturas2 * 2)
    area2 = (lados2 * alturas2)

    print("Perímetro:", perimetro1, "area:", area1)
    print("Perímetro:", perimetro2, "area:", area2)


if __name__ == "__main__":
    main()
