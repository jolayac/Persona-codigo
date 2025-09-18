from Contraseña import Contraseña


class Persona (nombre, edad):
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

    def mostrar_info(self):
        print(
            f"| Nombre: {self.nombre}.\n| Edad: {edad}.\n| Nº de identificación: {self.identificacion}.")


def main():

    pass


if __name__ == "__main__":
    main()
