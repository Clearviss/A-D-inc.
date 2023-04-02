#podstawa podstaw



print("witaj swiecie4")

#zmienne (tez podstawy)
a = 1
b = 2
print(a,b)

#!UWAGA! Bardzo przydatne
a = "dominik"
b = "rusinek"
print(f"twoje imie to {a} {b}")

#smykalki
a = "dominik"
duza_litera = a.title()
print(duza_litera)

b = "rusinek"
print(b.upper())
print(b.lower())

a = 14_000_000

a, b, c = 1, 2, 3

#stala no niby jest ale jej nie ma

#biale znaki
#   \t  <---  tab
#   \n  <---  znak nowego wiersza
#   .rstrip <---- usuwanie po prawej bialego znaku
#   .lstrip <---- usuwanie po lewej bialeog znaku
#   .strip <---- usuwanie po obydwu stronahc


#LISTY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
lista = [1,2,4,43]     #listy maja indeks od 0
#jezeli chcialnys zwrocic wartosc ostatnia nalezey wypisac -1
#operacje 
lista.append(32)
print(lista)
#dzieki insery beidze mzona zdefiniowac gdzie sie chce wlozyc dana wartosc do listy
lista.insert(0, "siematuwartosc")
print(lista)

#usuwanie
del lista[1]
print(lista)
#metoda pop do utrzymania wartosci po jej usunieciu przyklad na obcych
statek_xyz = [23,43,32]

popped_statek_xyz = statek_xyz.pop() #na pop tez dziala indeksowanie
print(statek_xyz)
print(popped_statek_xyz)
#remove sluzy do zlikwidowania wartosci poprzez jej nazwe
lista.remove(43)
print(lista)
#sortowianie
lista2 = ['dominik','lebron','adi']
lista2.sort() #ta metoda na stale przypisuje sortowanie do listy
print(lista2)
lista2.sort(reverse=True)
print(sorted(lista2))
#metoda reverse() odwraca liste
lista2.reverse()
print(lista2)
#len okresla ilosc elementow na liscie
print(len(lista2))

#PRACA Z LITSA PETLA FOR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
czlowieki = ['dominik', 'adrian', 'kuba', 'max']
for czlowiek in czlowieki:
    print(czlowiek)

for value in range(1,101):
    print(value)

#mozna utworzyc liste poprzez funkcje list()
liczby = list(range(1,11))
print(liczby)
#trzeci  argument w range sluzy do pomijania w ten sposob mozna np wypisac liczby parzyste
#istnieja funkcja dla liczb w listach
print(max(liczby))
print(min(liczby))
print(sum(liczby))

#lista skladana (hardcore)
listi = [value**2 for value in range(1,10)] #kwadraty liczb
for dane in listi:
    print(dane)

#fragmenty listy
lista3 = list(range(1,51))
print(lista3[41:51])
#jezeli zostanie podany tylko drugi argument lista wypisze tyle elementow ile wynosi argument
print(lista3[:11])
print(lista3[30:])
#z minusem po prostu na odwrot
#kopiowanie listy jest dosc proste
lista4 = lista3 
print(lista4) #jest to doslowna kopia i tym samym lista4 bedzie sie odnosic do listy3
lista5 = lista3[:] # a to utworzenie nowej listy
#obok listy w Pythonie stoi krotka (tuple) jest to lista ktorej nie mozna edytowac mozna jedynie przypisac calkowicie nowa wartosc 


#IF INSTRUKCJE WARUNKOWE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
a = 1
if a == 1:
    print(a)
else:
    print(a+2)
lista6 = ['dominik', 'adi', 'harden']
if 'harden' in lista6:
    print('mamy hardena')
else:
    print("nie mamy hardena")

#slowniki
alien_0 = {
    'color': 'green',
    'health': 100,
}

print(alien_0['color']) #analogiczne mozna robic ze slowinikiem te same rzeczy co z listą
#usuwanie nastepuje poprzez del
if alien_0['color'] == 'green':
    for alien in alien_0:
        print(alien)
#metoda get powoduje wartosc domyslna dla slownika 
#print(alien_0['points']) w tym wypadku wyskoczyl by bład poniewaz nie ma points w slowniku
print(alien_0.get('points', 'nie ma przypisanych punktow')) #jezeli w slowniku pojawia sie points to wypisze ich wartosc

for key, value in alien_0.items():
    print(f"alien {key} is {value}")

#WHILE do przenoszenia wartosci z listy do listy i usuwanie 
F_users = ['dominik', 'kuba', 'adi', 'max']
confirmed_users = []

while F_users:
    confirmed_user = F_users.pop()
    confirmed_users.append(confirmed_user)
    print(f"sprawdzam uzytkownika: {confirmed_user}")
for user in confirmed_users:
    print(f"sprawdzony uzytkownik: {user}")
#usuwanie
koty = ['perski', 'dachowiec', 'syjamski', 'zwykly','perski']
while 'perski' in koty:
    koty.remove('perski')
for kot in koty:
    print(kot)
#!!!!!!!!!!!!!!FUNKCJE!!!!!!!!!!!!!!!!#############!#!#!##!#!#!#!#!#!#!##!#!#!#!!!#!#!!#!#!#!#!#!#!##!#!#
def witaj():
    a = input("podaj imie: ")
    print(f'Witaj {a.title()}!')

def witaj2(a, b):
    name = f'{a} {b}'
    return name
a = 'dominik'
b = 'rusinek'
print(f'witaj {witaj2(a,b).title()}')

#za pomoca instrukcji warunkowych mozna zdeficiowac wartosc opjonalna

# * oznacza ze mozna dac wiele argumentow (tworzy tuple (krotke)) 
def pizza(*toppings):
    print(toppings)

pizza('pieczarki', 'pepperoni', 'szynka')
#krotka nadal bedzie utworzona nawet jesli zostanie podany jeden argument 

# ** oznacza dowolna klucz-wartosc 
# import modulow
import Modul
Modul.pizzamaker(32,'pieczarki','szynka','ser')
# from modul import funkcja | okreslona funkcja |
# from modul import funkcja as alias | funkjce mozna przypisac do poszczegolnych nazw popzrez "as"
# tyn samym w folderze tworzy sie folder _pycache_ odpowiedzialny za pamiec modulu
from Modul import pizzamaker as pm 
pm(32, "pieczarki", "szynka", "ser")
# za pomoca * mozna zaimportowac wszytkie funkjce
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# KLASY 
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\\
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#klasy sluza do modelowania 
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name.title()} teraz siedzi")
    def roll_over(self):
        print(f"{self.name.title()} teraz polozyl sie na plecach")

class Dog():
    my_dog = Dog("louis", 4)

    print(f'moj pies ma {my_dog.age} lata')
    my_dog.sit()
    my_dog.roll_over()
