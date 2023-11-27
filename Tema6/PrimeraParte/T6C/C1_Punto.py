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

    print("Coordenada x:", punto1.getX(), "Coordenada y:", punto1.getY())
    print("Coordenada x:", punto2.getX(), "Coordenada y:", punto2.getY())
    print("Coordenada x:", punto3.getX(), "Coordenada y:", punto3.getY())

    print("Segunda Parte")

    punto1.setX(5)
    punto1.setY(10)
    punto2.setX(3)
    punto2.setY(9)
    punto3.setX(6)
    punto3.setY(15)

    print("Coordenada x:", punto1.getX(), "Coordenada y:", punto1.getY())
    print("Coordenada x:", punto2.getX(), "Coordenada y:", punto2.getY())
    print("Coordenada x:", punto3.getX(), "Coordenada y:", punto3.getY())


if __name__ == "__main__":
    main()
