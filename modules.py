class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __repr__(self):
        return f"{self.suma}"
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __repr__(self):
        return f"Pajamos: {self.suma} (siuntėjas - {self.siuntejas}, info - {self.info}"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, budas, isigyta, info):
        super().__init__(suma)
        self.budas = budas
        self.isigyta = isigyta
        self.info = info

    def __repr__(self):
        return f"Išlaidos: {self.suma} (būdas - {self.budas}, įsigyta - {self.isigyta}, info - {self.info}"
