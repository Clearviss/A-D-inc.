# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(f'{self.name.title()} teraz siedzi!')
    
#     def roll(self):
#         print(f'{self.name.title()} teraz bedzie sie turlal!')

# from pydoc import describe


class Restuarant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'Restaracja {self.restaurant_name.title()} i jest typem {self.cuisine_type} ')

    def set_number_served(self, new_number):
        self.number_served = new_number
    
    def increment_number_served(self, clients_served):
        self.number_served += clients_served

class IceCreamStand(Restuarant):
    def __init__(self, restaurant_name, cuisine_type):
        self.flavors = ['Strawberry', 'Banana', 'Apple']
        super().__init__(restaurant_name, cuisine_type)

    def show_flavors(self):
        print("lista dostępnych smakow: ")
        for flavor in self.flavors:
            print(flavor)
            
    
ice = IceCreamStand('res', 'icecream')
ice.show_flavors()






# restaurant = Restuarant('restauracja zajebista', 'indyjska')
# restaurant.set_number_served(100)
# restaurant.increment_number_served(23)
# restaurant.increment_number_served(132)

# obsluzeni = restaurant.number_served
# print(f"Dzisiaj obsluzono {obsluzeni} klientow")











# moja_restauracja = Restuarant("vespuci", 'włoska')
# twoja_restauracja = Restuarant("vicollo", 'chinska')
# naj_restauracja = Restuarant('michelin', 'prestizowa')

# restauracje = [moja_restauracja, twoja_restauracja, naj_restauracja]

# for restauracja in restauracje:
#     restauracja.describe_restaurant()












# import random

# # imia = ['dominik', 'adrian', 'maks', 'kuba', 'aleks']
# # nazwiska = ['rogulski', 'cichowski', 'ernst', 'zborala', 'rusinek']

# class User():
#     def __init__(self):
#         imia = ['dominik', 'adrian', 'maks', 'kuba', 'aleks']
#         nazwiska = ['rogulski', 'cichowski', 'ernst', 'zborala', 'rusinek']
#         los = random.randint(0, 4)
#         los2 = random.randint(0, 4)
#         self.first_name = imia[los]
#         self.last_name = nazwiska[los2]
#         self.loginAttempts = 0
    

#     def describeUser(self):
#         print(f"Witaj {self.first_name.title()}, zgaduję że twoje nazwisko to {self.last_name}")
        
#     def greetUser(self):
#         print(f"Witaj {self.first_name.title()} {self.last_name.title()}")
    
#     def increment_userLogins(self):
#         self.loginAttempts += 1
    
#     def reset_LoginsAttempts(self):
#         self.loginAttempts = 0


# user = User()
# user.describeUser()



    

        