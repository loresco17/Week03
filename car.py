class Car: #Definisco un nuovo tipo di dato, la classe (con lettera maiusc)
    wheels=4 # Variabile di classe, identica per tutte le istanze di quella classe
    def __init__(self, license_plate, color):
        self.licensePlate=license_plate #Attributi o variabili di istanza
        self.bodyColor=color
        self.turnedOn=False

    def paint(self, color):
        self.bodyColor=color

    def turnOn(self):
        self.turnedOn=True


c1=Car('AA123BB', 'Red') #Creo un oggetto/istanza

print(f"License plate: {c1.licensePlate}") #Stampo uno a uno gli attributi dell'istanza
print(f"Color: {c1.bodyColor}")
print(f"Turned on: {c1.turnedOn}")

c2=Car('ZZ666ZZ', 'Black')

c1.color='Green' #Accedere alle variabili di istanza
Car.wheels=7 #Accedere alle variabili di classe

c2.paint('Violet') #Accedere alle variabili di istanza tramite funzioni
c1.turnOn()

c1.number_of_doors=2 #Si possono definire delle altre variabili scrivendo nome_oggetto.nome_attributo, ma sarà propria esclusivamente di quell'oggetto