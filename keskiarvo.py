import math
from math import *
print("Arvosanalaskuri")
while True:
    pisteet = float(input("Oppilaan saamat pisteet: "))
    maksimipisteet = float(input("Maksimipisteet: "))
    alaraja = float(input("Nelosen alaraja: "))
    if pisteet < alaraja:
        arvosana = 4
    elif maksimipisteet < alaraja:
        arvosana = 4
    elif pisteet > maksimipisteet:
        arvosana = 10.25
    else:
        def round_up(n, decimals=0):
            multiplier = 10 ** decimals
            return math.ceil(n * multiplier) / multiplier
        arvosana = round_up((((pisteet-alaraja)/(maksimipisteet-alaraja))*6+4), 1)
    def round(arvosana):
        #DEBUGGAAMISTA VARTEN
        #print(arvosana*10-math.floor(arvosana)*10)
        leftover = arvosana*10-math.floor(arvosana)*10
        print(leftover)
        if leftover < 1.25:
            print(1)
            arvosana = math.floor(arvosana)
        elif leftover < 3.75:
            print(2)
            arvosana = math.floor(arvosana) + 0.25
        elif leftover < 6.25:
            print(3)
            arvosana = math.floor(arvosana) + 0.5           
        elif leftover*10 < 8.75:
            print(4)
            arvosana = math.floor(arvosana) + 0.75
        else:
            print(5)
            arvosana = int(arvosana) + 1
        return arvosana
    round(arvosana)
            
                       
    print("Oppilaan arvosana: " + str(arvosana))
    print("")
