class Persona:
    __MAYORIA_EDAD = 18

    def __init__(self, dni, nombre, apellidos, edad):
        self.__DNI = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_edad(self, edad):
        self.__edad = edad

    # Getters
    def get_dni(self):
        return self.__DNI

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_edad(self):
        return self.__edad

    # Métodos

    def mayoria_edad(self):
        if self.__edad >= Persona.__MAYORIA_EDAD:
            return True
        else:
            return False

    def jubilado(self):
        if self.__edad >= 65:
            return True
        else:
            return False

    def diferencia_edad(self, p):
        if self.__edad - p.get_edad() < 0:
            abs(self.__edad - p.get_edad())
        else:
            return self.__edad - p.get_edad()

    def imprimir(self):
        if self.get_edad() >= Persona.__MAYORIA_EDAD:
            print(self.get_apellidos(), self.get_nombre(), "con DNI:", self.get_dni(), "es mayor de edad")
        elif self.get_edad() < Persona.__MAYORIA_EDAD:
            print(self.get_apellidos(), self.get_nombre(), "con DNI:", self.get_dni(),
                  "no es mayor de edad")
        elif self.get_edad() >= 65:
            print(self.get_apellidos(), self.get_nombre(), "con DNI:", self.get_dni(), "es un jubilado")


def main():
    persona1 = Persona(str(input()), str(input()), str(input()), int(input()))
    persona2 = Persona(str(input()), str(input()), str(input()), int(input()))

    persona1.imprimir()
    persona2.imprimir()

    print("Diferencia de edad:")

    persona1.diferencia_edad(persona2)
    persona2.diferencia_edad(persona1)

    print("Es mayor de edad:")

    print(persona1.mayoria_edad())
    print(persona2.mayoria_edad())

    print("Es jubilado:")

    print(persona1.jubilado())
    print(persona1.jubilado())


if __name__ == "__main__":
    main()
