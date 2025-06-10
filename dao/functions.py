# dao/functions.py

# Data Access Object para zapatos

class ZapatoDao:
    def __init__(self):
        self.zapatos = []

    def add(self, zapato):
        self.zapatos.append(zapato)

    def show(self):
        for zapato in self.zapatos:
            print(zapato)
