
while True:
    base = int(input("Haluatko binääristä kymmenjärjestelmään (1) vai kymmenjärjestelmästä binääriin (2)?:  "))
    print("Kirjoita break jos haluat valita uudestaan.")
    if base == 1:
        while True:
            num1 = int(input("Anna binääriluku (esimerkiksi 01010): "))
            num2 = 0
            pituus = len(str(num1))
            x = 0
            for i in range(0,pituus):
                if str(num1)[x] == "1":
                    num2 += 2 ** (pituus - 1 - x)
                x += 1

            print(str(num1) + " on kymmenjärjestelmässä " + str(num2))
    elif base == 2:
        while True:
            num3 = input("Anna luku kymmenjärjestelmässä: ")
            if num3 == "break":
                break
            print(str(num3) + " on binäärissä " + str(int(bin(int(num3))[2:])))
