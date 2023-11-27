class Articulo:
    def __init__(self, nombre, precio, iva, cuantos_quedan):
        self.__nombre = nombre
        self.__precio = precio
        self.__iva = iva
        self.__cuantos_quedan = cuantos_quedan

    # Setters

    def set_nombre(self, nombre):
        if nombre == "":
            print("Error al establecer nombre")
        else:
            self.__nombre = nombre

    def set_precio(self, precio):
        if precio <= 0:
            print("Error al establecer precio")
        else:
            self.__precio = precio

    def set_iva(self, iva):
        if iva != 21:
            print("Error al establecer IVA")
        else:
            self.__iva = iva

    def set_inventario(self, cuantos_quedan):
        if cuantos_quedan < 0:
            print("Error al establecer inventario")
        self.__cuantos_quedan = cuantos_quedan

    # Getters

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_iva(self):
        return self.__iva

    def get_inventario(self):
        return self.__cuantos_quedan


def main():
    articulo1 = Articulo("Pijama BobEsponja", 10, 21, 10)
    articulo2 = Articulo("Pijama Batman", 16, 21, 3)

    pvp1 = articulo1.get_iva() / 100 * articulo1.get_precio() + articulo1.get_precio()
    pvp2 = articulo2.get_iva() / 100 * articulo2.get_precio() + articulo2.get_precio()

    print(articulo1.get_nombre(), "- Precio:", articulo1.get_precio(), "€ - IVA:", articulo1.get_iva(), "% - PVP:",
          pvp1, "€")
    print(articulo2.get_nombre(), "- Precio:", articulo2.get_precio(), "€ - IVA:", articulo2.get_iva(), "% - PVP:",
          pvp2, "€")


if __name__ == "__main__":
    main()
