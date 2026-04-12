class Computador:
    def __init__(self, processador, memoria):
        
        self.processador = str(processador)
        self.memoria = int(memoria)

class Laptop(Computador):
    def __init__(self, processador, memoria, bateria_watts=0):
        super().__init__(processador, memoria)
        self.bateria_watts = bateria_watts

class Desktop(Computador):
    def __init__(self, processador, memoria, gabinete=''):
        super().__init__(processador, memoria)
        self.gabinete = str(gabinete)

l1 = Laptop("i7", 16, 50)
d1 = Desktop("i9", 32, "Gamer")

print("=== Laptop ===")
print(f"Processador: {l1.processador}")
print(f"Memória: {l1.memoria}GB")
print(f"Bateria: {l1.bateria_watts}W")

print("\n=== Desktop ===")
print(f"Processador: {d1.processador}")
print(f"Memória: {d1.memoria}GB")
print(f"Gabinete: {d1.gabinete}")