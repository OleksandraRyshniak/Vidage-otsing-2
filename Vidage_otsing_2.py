

print("*** Arvude mäng ***")

# Kasutajalt numbri taotlemine
while True:
    try:
        a = abs(int(input("Sisesta täisarv => ")))
        break
    except ValueError:
        print("See ei ole täisarv")

# Kontrollida, kas number ei ole null
if a == 0:
    print("Nulliga on mõttetu töötada")
else:
    print("Loendame, mitu on paaris ja mitu paaritut arvu")
    c = b = a
    paaris = 0
    paaritu = 0
    while b > 0:
        if b % 2 == 0: 
            paaris += 1
        else:
            paaritu += 1
        b = b // 10
    print(f"Paaris arvude kogus: {paaris}")
    print(f"Paaritute arvude kogus: {paaritu}")
    print()
    # kui palju paaris- ja paarituid arve
    print("*Ümberpöörame* sisestatud arvu")
    b = 0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10 + number
    print(f"*Ümberpööratud* arv: {b}")
    #ümberpöörates 
    print("Tõestame teoreemi")
    if c % 2 == 0:
        print("c - Paaris arv, jagame 2")
    else:
        print("c - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
        if c % 2 == 0:
            print('{:>4}'.format(round(c)),"с - Paaris arv, Jagame 2")
            c //= 2 
        else:
            print('{:>4}'.format(round(c)),"с - Paaritu arv.Korrutame 3, liidame 1 ja jagame 2.")
            c = (3 * c + 1) // 2  
            print(c, end=" ")
    print()
    print("Teoreem on tõestatud")



   
