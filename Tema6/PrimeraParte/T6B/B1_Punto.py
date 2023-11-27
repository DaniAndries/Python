class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def main():
    punto1 = Punto(5, 0)
    punto2 = Punto(10, 10)
    punto3 = Punto(-3, 7)

    print("Coordenada x:", punto1.x, "Coordenada y:", punto1.y)
    print("Coordenada x:", punto2.x, "Coordenada y:", punto2.y)
    print("Coordenada x:", punto3.x, "Coordenada y:", punto3.y)

    print("Segunda Parte")

    punto1 = Punto(2+5, 0+2)
    punto2 = Punto(5/10, 5/10)
    punto3 = Punto(-3+6, 7-6)

    print("Coordenada x:", punto1.x, "Coordenada y:", punto1.y)
    print("Coordenada x:", punto2.x, "Coordenada y:", punto2.y)
    print("Coordenada x:", punto3.x, "Coordenada y:", punto3.y)


if __name__ == "__main__":
    main()
