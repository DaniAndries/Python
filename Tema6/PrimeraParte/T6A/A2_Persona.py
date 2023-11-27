class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad


def main():
    persona1 = Persona(str(input()), str(input()), str(input()), int(input()))
    persona2 = Persona(str(input()), str(input()), str(input()), int(input()))

    if persona1.edad >= 18:
        print(persona1.apellidos, persona1.nombre, "con DNI:", persona1.dni, "es mayor de edad")
    else:
        print(persona1.apellidos, persona1.nombre, "con DNI:", persona1.dni, "no es mayor de edad")

    if persona2.edad >= 18:
        print(persona2.apellidos, persona2.nombre, "con DNI:", persona2.dni, "es mayor de edad")
    else:
        print(persona1.apellidos, persona1.nombre, "con DNI:", persona1.dni, "no es mayor de edad")


if __name__ == "__main__":
    main()
