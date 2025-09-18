class Contraseña:
    def __init__(self, contraseña):
        self.contraseña = contraseña

    def crear_contraseña(self, contraseña):
        while True:
            print(
                "Ingrese una contraseña.\nTenga en cuenta que la contraseña debe cumplir con lo siguinte:")
            input(
                "-Mínimo 8 caracteres.\n-Combinar mayúsclas y minúsculas.\nTener un caracter especial.")
            if len(contraseña) < 8:
                print(
                    "La contraseña debe tener 8 caracteres como mínimo.\nIntente de nuevo.\n>")
