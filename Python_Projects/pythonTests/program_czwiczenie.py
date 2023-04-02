# # # imie = input('podaj imie: ')
# # # nazwisko = input('podaj nazwisko: ')

# # # imie = imie.title()
# # # nazwisko = nazwisko.title()

# # # imie_nazwisko1 = imie+' '+nazwisko
# # # print(f'twoje imie i nazwisko to {imie_nazwisko1}')

# # # ludzie = []
# # # ludzie.append(imie_nazwisko1)
# # # print(ludzie[0])

# # # kwadraty = []
# # # for kwadrat in range(1,11):
# # #     kwadraty.append(kwadrat**2)

# # # for liczba in kwadraty:
# # #     print(liczba)

# # alien_0 = {
# #     'color': 'green',
# #     'health': 100,
# # }

# # punkty = list(range(1, alien_0['health']))
# # print(punkty)

# sandwich_orders = ['tuńczyk', 'szynka', 'ogorek', 'subway']
# finished_sandwich = []
# while sandwich_orders:
#     finished = sandwich_orders.pop()
#     finished_sandwich.append(finished)
# for sandwich in finished_sandwich:
#     print(f"przygtowano kanapke {sandwich}")


class Restaurant():
    def __init__(self, restaurant_name, cruisine_type):
        self.restaurant_name = restaurant_name
        self.cruisine_type = cruisine_type
    def describe(self):
        print(f"restauracja nazywa sie {self.restaurant_name.title()} i jest typu {self.cruisine_type} ")
    def open(self, godzina):
        print(f'restauracja otwarta jest w godzinach {godzina}')
class Restaurant():
    mojares = Restaurant(input("podaj nazwe: "), input("podaj typ: "))
    print(mojares.restaurant_name)
    print(mojares.cruisine_type)
    mojares.describe()
    mojares.open(input("podaj godzinevi"))
    