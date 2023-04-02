# range = [1,2,3,4,5]
# for value in range:
#     print(value)

# for value in range(1,1001):
#     print(value)

aliens = []

for alien in range(1,31):
    alien = {
        'color': 'green',
        'hp': 75
    }
    aliens.append(alien)
print(aliens)
for value in aliens:
    print(value.get('kolor', 'brak koloru'))
    