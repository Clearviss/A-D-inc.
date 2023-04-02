def pizzamaker(size, *topping):
    print(f"przygotowuje pizze o wiellkosci {size} i skladnikami:")
    for top in topping:
        print(f'- {top}')