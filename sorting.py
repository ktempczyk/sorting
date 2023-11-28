import random

x = input("Podaj ilosc liczb losowych do wygenerowania i posortowania: ")
x=int(x)

zbior_liczb_losowych = []

for i in range (0,x):
    zbior_liczb_losowych.insert((0+i),random.randint(0,100))

print ("Oto twoje liczby losowe przed sortowaniem: " + str(zbior_liczb_losowych))

posortowany_zbior_liczb_losowych = []

for i in range (0,x):
    y = min(zbior_liczb_losowych)
    zbior_liczb_losowych.remove(y)
    posortowany_zbior_liczb_losowych.insert((0+i),y)
    

print ("Oto twoje liczby losowe po sortowaniu: " + str(posortowany_zbior_liczb_losowych))