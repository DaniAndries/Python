class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.x2 > self.x1 and self.y2 > self.y1:
            print("Error al establecer los valores")

def main():
    rectangulo1 = Rectangulo(0, 0, 5, 5)
    rectangulo2 = Rectangulo(7, 9, 2, 3)

    lados1 = (rectangulo1.x2 - rectangulo1.x1)
    alturas1 = (rectangulo1.y2 - rectangulo1.y1)
    perimetro1 = (lados1 * 2 + alturas1 * 2)
    area1 = (lados1 * alturas1)

    lados2 = (rectangulo2.x2 - rectangulo2.x1)
    alturas2 = (rectangulo2.y2 - rectangulo2.y1)
    perimetro2 = (lados2 * 2 + alturas2 * 2)
    area2 = (lados2 * alturas2)

    print("Perímetro:", perimetro1, "area:", area1)
    print("Perímetro:", perimetro2, "area:", area2)

    print("Parte 2")

    rectangulo1.x1 = 8
    rectangulo1.y1 = 10
    rectangulo1.x2 = 9
    rectangulo1.y2 = 6

    rectangulo2.x1 = 1
    rectangulo2.y1 = 2
    rectangulo2.x2 = 3
    rectangulo2.y2 = 4

    lados1 = (rectangulo1.x2 - rectangulo1.x1)
    alturas1 = (rectangulo1.y2 - rectangulo1.y1)
    perimetro1 = (lados1 * 2 + alturas1 * 2)
    area1 = (lados1 * alturas1)

    lados2 = (rectangulo2.x2 - rectangulo2.x1)
    alturas2 = (rectangulo2.y2 - rectangulo2.y1)
    perimetro2 = (lados2 * 2 + alturas2 * 2)
    area2 = (lados2 * alturas2)

    print("Perímetro:", perimetro1, "area:", area1)
    print("Perímetro:", perimetro2, "area:", area2)


if __name__ == "__main__":
    main()
