airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]
print('Lista dostepnych lotnisk: ')
for x in airports:
    print(x, end=', ')
print(" ")
print("a to wszystkie mozliwe połączenia: ")
for x in routes:
    print(f"{x[0]} - {x[1]}")
print('Podaj alias lotniska na którym się znajdujesz: ')
start = input()
print('Podaj alias lotniska na które chcesz się dostać: ')
destination = input()
t = False
loty = 0
lotyy = []
lotyy.append(start)

while(start!=destination):
    for key in routes:
        for x in key:
            if x==start:
                if start == key[1]:
                    start = key[0]
                    loty+=1
                    lotyy.append(start)
                else:
                    start = key[1]
                    loty+=1
                    lotyy.append(start)
                    t = True
                    break
print(f"Musisz dokonać {loty} lotów. lista przesiadek: ")
for x in lotyy:
    print(x) 


if t==False:
    print('nie ma pary')