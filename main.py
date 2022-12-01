import random
import time
print("Rozpoczynamy gre!")
time.sleep(1.5)
print("Zasady są proste:")
time.sleep(1.5)
print("Każdy gracz wybiera liczby z zakresu od 1 do 100")
time.sleep(1.5)
print("Następnie losujemy liczby z tego samego zakresu, wylosowana liczba jest usunięta z liczb każdego z graczy")
time.sleep(1.5*2)
print("Pierwsza osoba która pozbędzie się wszystkich wygrywa WSZYSTKO")
time.sleep(1.5*3)
for char in "gotowi?":
    print(char, end="")
    time.sleep(0.5)
print()
time.sleep(1.5)
gracze = int(input("podaj ilość graczy \n"))
ilosc_liczb = int(input("Podaj ilość liczb do wylosowania dla graczy \n"))
liczby_graczy = []
imiona_graczy = []
def liczby_takie_same():
    tmp_liczby = liczby_graczy[::]
    tmp_imiona = imiona_graczy[::]
    for i in range(len(tmp_liczby)):
        if tmp_liczby.count(tmp_liczby[i]) == 1:
            del tmp_imiona[i], tmp_liczby[i]
    return tmp_imiona
for i in range(gracze):
    imiona_graczy.append(input("Podaj imie gracza nr:"+str(i+1)+"\n"))
    liczby_graczy.append([])
    print("gracz",i, ":")
    j = 0
    while j<ilosc_liczb:
        try:
            liczby_graczy[i].append(int(input(str(j+1)+":\n")))
        except Exception:
            print("Bad number try again")
            continue
        j+=1
    powtarzajace_sie = liczby_takie_same()
    if len(powtarzajace_sie) != 0:
        print("liczby graczy", end=" ")
        for imie in powtarzajace_sie:
            print(imie, end=", ")
        print()
        print("Są takie same!!!")
        raise Exception("tak niewolno pobite gary")

def gracz_wygral():
    for gracz in liczby_graczy:
        if len(gracz) == 0:
            return True
    return False

while not gracz_wygral():
    x = random.randint(0, 100)
    counter = 0
    for gracz in liczby_graczy:
        if x in gracz:
            gracz.remove(x)
            counter += 1
    print("Liczba wylosowana to:",x, "trafiłą w:", counter, "graczy")
    time.sleep(0.25)
print("Koniec gry")
print("Podsumowywanie gry...")
time.sleep(5)
zwycięscy = []
for index in range(len(liczby_graczy)):
    if len(liczby_graczy[index]) == 0:
        zwycięscy.append(imiona_graczy[index])
if len(zwycięscy) == 1:
    print("Wygrał", zwycięscy[0])
    print("UwU")
elif len(zwycięscy) > 1:
    print("Remis Senpai!!!")
    print("Wygrał:")
    for i in zwycięscy:
        print(i, "oraz")

print()
print("Reszta graczy możę i była blisko:")
for imie_index in range(len(imiona_graczy)):
    print(imiona_graczy[imie_index], "-", end=" ")
    if len(liczby_graczy[imie_index]) == 0:
        print("nic, wygrał lol")
    else:
        for liczba in liczby_graczy[imie_index]:
            print(liczba, end=" ")
        print()