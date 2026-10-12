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
# Definisco un nuovo tipo di dato, la classe Car

# Per convenzione le classi hanno iniziale maiuscola
class Car:
    wheels = 4 # Variabile di classe, identica per tutte le istanze di quella classe

    # Creazione ed inizializzazione dell'oggetto con/in __init()__
    def __init__(self, license_plate, color): # Costruttore della classe
        self.license_plate = license_plate # Attributi o variabili di istanza
        self.color = color
        self.turned_on = False # Non mi servono necessariamente parametri
                               # per inizializzare tutti gli attributi, ma
                               # è buona norma comunque fornire una qualche
                               # inizializzazione per tutti

    # Metodi (ovvero le funzioni messe a disposizione di una classe)
    def paint(self, color):
        self.color = color

    def turn_on(self):
        self.turned_on=True


# Dopo aver definito la classe posso creare oggetti di quel tipo, usando la
# classe come una sorta di "stampino", tutti gli oggetti avranno quella struttura

# c1 = Car() # Creo un oggetto di classe/tipo Car

# Se ho definito parametri, posso creare l'oggetto passandoli al costruttore

c1 = Car("AA123BB","Red")

# print(c1) # Se la stampa senza accorgimenti particolari vedrò il riferimento (memoria)

# Per stampare il contenuto dell'oggetto e non il riferimento devo usare il .

print("License plate: "+str(c1.license_plate))
print("Color: "+str(c1.color))
print("Turned on: "+str(c1.turned_on))

# Posso creare altre istanze/oggetti, ciascuno con proprie copie degli attributi

c2 = Car("ZZ666ZZ", "Black")

# Come si accede agli attributi/alle variabili di istanza? Con . sul nome dell'oggetto
c1.color = "Green"

# Come si accede alle variabili di classe? Con . sul nome della classe
Car.wheels = 7

# E se scrivo ...?

c1.number_of_doors = 2 # E' una variabile di classe, di istanze, oppure ...?

# Il programmatore può, tipicamente per sbaglio, andare a definire delle altre
# variabili scrivendo nome_oggetto.nome_variabile, ma quella sarà propria
# solo di quella istanza e non di tutti gli oggetti creati a partire da
# quella classe (non sarà né un attributo né una variabile di classe)

# Come faccio a cambiare il colore di un oggetto Car? O lo stato di accensione?

c1.color = "Pink"
c2.turned_on = True

# Anziché accedere direttamente agli attributi, posso usare le funzioni

c1.paint("Violet")
c2.turn_on()











