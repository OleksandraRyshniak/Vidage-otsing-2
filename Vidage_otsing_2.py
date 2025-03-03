
from asyncio import sleep


print("*** Arvude mäng ***")
print()
#название игры
while 1:
    try:
        a=abs(int(input("Sisesta täisarv => ")))
        break
    except ValueError:
         print("See ei ole täisarv")
#введение числа
if a==0:
    print("Nulliga on mõttetu töö")
else:
#---
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
            if b % 2 == 0:
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b = b//10
    print(f"Paaris arvude kogus:{paaris}")
    print(f"Paaritu on:{paaritu}")
    print()
#'''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Ümberpööratud", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreem")
    print()
    if c % 2 == 0:
        print("с - Paaris arv, Jagame 2")
    else:
        print("с - Paaritu arv.Korrutame 3, liidame 1 ja jagame 2.")
    for i in range(50):
        print(">", end="")
        sleep(0.5)
    print()
    while c != 1:
        sleep(1)
        if c % 2 == 0:
            print('{:>4}'.format(round(c)),"с - Paaris arv, Jagame 2")
            c == c / 2
            else:
                    c == (3*c + 1) / 2
            print("c, end=")
    print()
    print("Гипотеза верна")

   