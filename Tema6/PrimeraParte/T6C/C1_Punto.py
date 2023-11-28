class Punto:
    def __init__(self, x=0, y=0):
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


def main():
    punto1 = Punto(5, 0)
    punto2 = Punto(10, 10)
    punto3 = Punto(-3, 7)

    print("Coordenada x:", punto1.get_x(), "Coordenada y:", punto1.get_y())
    print("Coordenada x:", punto2.get_x(), "Coordenada y:", punto2.get_y())
    print("Coordenada x:", punto3.get_x(), "Coordenada y:", punto3.get_y())

    print("Segunda Parte")

    punto1.set_x(5)
    punto1.set_y(10)
    punto2.set_x(3)
    punto2.set_y(9)
    punto3.set_x(6)
    punto3.set_y(15)

    print("Coordenada x:", punto1.get_x(), "Coordenada y:", punto1.get_y())
    print("Coordenada x:", punto2.get_x(), "Coordenada y:", punto2.get_y())
    print("Coordenada x:", punto3.get_x(), "Coordenada y:", punto3.get_y())


if __name__ == "__main__":
    main()
