def collatz(number):
    if (number%2)==0:
        w = number//2
        print(w)
        return w
    else:
        w = 3*number + 1
        print(w)
        return w
    
inp = int(input("podaj liczbe: "))
print(inp)
while inp!=1:
    inp = collatz(inp)