class Articulo:
    def __init__(self, nombre, precio, iva, cuantos_quedan):
        self.nombre = nombre
        self.precio = precio
        self.iva = iva
        self.cuantos_quedan = cuantos_quedan


def main():
    articulo1 = Articulo("Pijama BobEsponja", 10, 21, 10)
    articulo2 = Articulo("Pijama Batman", 16, 21, 3)

    pvp1 = articulo1.iva / 100 * articulo1.precio + articulo1.precio
    pvp2 = articulo2.iva / 100 * articulo2.precio + articulo2.precio

    print(articulo1.nombre, "- Precio:", articulo1.precio, "€ - IVA:", articulo1.iva, "% - PVP:", pvp1, "€")
    print(articulo2.nombre, "- Precio:", articulo2.precio, "€ - IVA:", articulo2.iva, "% - PVP:", pvp2, "€")


if __name__ == "__main__":
    main()
