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