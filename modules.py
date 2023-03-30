class Irasas:
    def __init__(self, suma, tipas):
        self.suma = suma
        self.tipas = tipas
    def __repr__(self):
        return f"{self.tipas}: {self.suma}"

# irasas = Irasas(100, "Pajamos")
# irasas2 = Irasas(10, "Išlaidos")