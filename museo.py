from quadro import Quadro #Se voglio utilizzare una classe definita in un altro file devo usare la forma import 'file' from 'classe'

q=Quadro('Monet', '...', '...', '...') #Posso utilizzare la classe Quadro per creare oggetti

print(q.__str__()) #Posso usare le funzioni definite nella classe Quadro
print(q) #Se ho definito la funzione --str-- per l'oggetto python capisce che deve utilizzare quella funzione anziché stampare l'indirizzo di memoria

lista_quadri=[]
lista_quadri.append(q)
lista_quadri.append(Quadro('Cezanne', '...', '...', '...'))
lista_quadri.append(Quadro('Pollock', '...', '...', '...'))
print("Lista di quadri:")
for quadro in lista_quadri:
    print(quadro)