class Articulo:
    iva = 21
    iva_reducido = 10
    iva_super_reducido = 4

    def __init__(self, nombre, precio, cuantos_quedan, tipo_iva):
        self.__nombre = nombre
        self.__precio = precio
        self.__cuantos_quedan = cuantos_quedan
        if tipo_iva == 1:
            self.__tipo_iva = Articulo.iva
        elif tipo_iva == 2:
            self.__tipo_iva = Articulo.iva_reducido
        elif tipo_iva == 3:
            self.__tipo_iva = Articulo.iva_super_reducido
        else:
            self.__tipo_iva = Articulo.iva
            print("Error al establecer el iva")

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
        return self.__tipo_iva

    def get_inventario(self):
        return self.__cuantos_quedan

    # Métodos

    def get_pvp(self):
        return self.get_iva() / 100 * self.get_precio() + self.get_precio()

    def get_descuento_pvp(self, descuento):
        return descuento / 100 * self.get_precio() - self.get_precio()

    def vender(self, x):
        if self.__cuantos_quedan - x < 0:
            return False
        else:
            self.__cuantos_quedan -= x
            return True

    def almacenar(self, x):
        if self.__cuantos_quedan + x < 0:
            return False
        else:
            self.__cuantos_quedan += x
            return True

    def imprimir(self):
        print(self.get_nombre(), "- Precio:", self.get_precio(), "€ - IVA:", self.get_iva(), "% - PVP:", self.get_pvp(),
              "€")


def main():
    articulo1 = Articulo("Pijama BobEsponja", 10, 21, 1)
    articulo2 = Articulo("Pijama Batman", 16, 21, 1)
    articulo3 = Articulo("Pijama BatmanEsponja", 10, 21, 2)
    articulo4 = Articulo("Pijama BobBatman", 16, 21, 2)

    articulo1.imprimir()
    articulo2.imprimir()
    articulo3.imprimir()
    articulo4.imprimir()

    articulo1.almacenar(5)
    articulo2.almacenar(5)

    print(articulo1.get_inventario())
    print(articulo2.get_inventario())

    articulo1.vender(3)
    articulo2.vender(1)

    print(articulo1.get_inventario())
    print(articulo2.get_inventario())

    articulo1.get_descuento_pvp(21)
    articulo2.get_descuento_pvp(21)

    articulo1.imprimir()
    articulo2.imprimir()


if __name__ == "__main__":
    main()
