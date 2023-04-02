# with open('pi.txt') as file_object:
#     content = file_object.read()
# print(content)


ilosc = int(input("ile imion cchcesz podac?"))
a = 0

with open("guests.txt", 'a') as file_object:
    while(a<=ilosc):
        guest = input("podaj imie: ")
        file_object.write("\n"+guest)
        a=a+1

with open('guests.txt') as file_object:
    zmienna = file_object.read()
print(zmienna)