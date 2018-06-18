import time


class Coche:
    
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print ("Se han introducido", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print ("El coche se encuentra en movimiento.")
        else:
            print ("El coche no arranca...")

    def conducir(self):
        while self.gasolina > 0:
            
            time.sleep(1)
            print ("Quedan", self.gasolina, "litros")
            self.gasolina=self.gasolina-1
        
        if self.gasolina ==0:
            print ("El coche esta sin combustible.")



mi_coche2=Coche(gasolina=int(input("Cuantos litros de gasolina desea: ")))
mi_coche2.arrancar()
mi_coche2.conducir()