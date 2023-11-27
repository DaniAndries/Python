class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

    # Setters
    def set_dni(self, dni):
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_edad(self, edad):
        self.__edad = edad

    # Getters
    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_edad(self):
        return self.__edad


def main():
    persona1 = Persona(str(input()), str(input()), str(input()), int(input()))
    persona2 = Persona(str(input()), str(input()), str(input()), int(input()))

    if persona1.get_edad() >= 18:
        print(persona1.get_apellidos(), persona1.get_nombre(), "con DNI:", persona1.get_dni(), "es mayor de edad")
    else:
        print(persona1.get_apellidos(), persona1.get_nombre(), "con DNI:", persona1.get_dni(), "no es mayor de edad")

    if persona2.get_edad() >= 18:
        print(persona2.get_apellidos(), persona2.get_nombre(), "con DNI:", persona2.get_dni(), "es mayor de edad")
    else:
        print(persona1.get_apellidos(), persona1.get_nombre(), "con DNI:", persona1.get_dni(), "no es mayor de edad")


if __name__ == "__main__":
    main()
