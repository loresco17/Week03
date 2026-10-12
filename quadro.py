class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista=artista #Attributi privati (_ per scoraggiare, __per bloccare l'accesso)
        self.__titolo=titolo
        self.__materiali=materiali
        self.__anno=anno

    @property #Metodo per leggere il valore degli attributi nascosti
    def anno(self):
        return self.__anno
    @anno.setter #Metodo per impostare il valore degli attributi nascosti
    def anno(self, anno):
        self.__anno=anno

    def __str__(self): #Metodo che crea una stringa con tutti gli attributi del quadro in una stringa
        return f"{self.__artista}, {self.__titolo}, {self.__materiali}, {self.anno}"
q1=Quadro('Van Gogh', 'Autoritratto', 'Olio su tela',1870)

#q1.__anno=1945 Non posso farlo perchè l'attributo è privato
#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

print(f'Anno: {q1.anno}')

print(q1.__str__())
    # Metodo/Funzione che costruisce gli oggetti di classe Quadro e li inizializza
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista # Privati/Nascosti (con _ per scoraggiare o __ per bloccare l'accesso)
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno #1853 e 1890

    # Altri metodi, es. getter/setter per l'accesso agli attrributi in lettura e scrittura

    # Metodo per leggere il valore dell'attributo nascosto anno (metodo getter)
    @property
    def anno(self):
        return self.__anno

    # Metodo per impostare il valore dell'attributo nascosto anno (metodo setter)
    @anno.setter
    def anno(self, anno):
        self.__anno = anno # Eventualmente posso aggiungere codice per controllo errori

    # Metodo/Funzione che consente al quadro di descriversi come stringa
    # __str__ come alternativa a nomi più bizzarri come descriviti(), ...
    def __str__(self):
        return f"{self.__artista}, {self.__titolo}, {self.__materiali}, {self.__anno}"



q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

# q1.__anno = 1945 # Non posso farlo così perché l'attributo è privato/nascosto

# Per accedere all'attributo devo usare i metodi/le funzioni

# q1.imposta_anno(1800)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

# print("Anno:"+str(q1.leggi_anno()))

print("Anno: " + str(q1.anno))

# Come faccio a stampare il quadro

print(q1)

# print(q1.__artista)

# Chi meglio del quadro sa come stamparsi?

# print(q1.descriviti()) # Ho DELEGATO al quadro il compito di stamparsi

print(q1.__str__())


q1.anno = 5 # Python usa il metodo setter/getter per
            # accedere agli attributi, se definiti

print(q1.anno)

# Equivalentemente, posso usare i metodi getter, con ()
q1.anno(5)
print(q1.anno())
