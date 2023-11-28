from Tema6.PrimeraParte.T6D.D1_Punto import Punto


class Triangulo:
    p1 = Punto
    p2 = Punto
    p3 = Punto

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimetro(self):
        print(self.p1.distancia(self.p2) + self.p2.distancia(self.p3) + self.p3.distancia(self.p1))


def main():
    punto1 = Punto(4, 6)
    punto2 = Punto(2, 4)
    punto3 = Punto(3, 9)

    triangulo1 = Triangulo(punto1, punto2, punto3)

    triangulo1.perimetro()


if __name__ == "__main__":
    main()
