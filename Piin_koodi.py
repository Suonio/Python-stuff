#Importoidaan tarvittavat jutut
import random

#Tervetulotoivotus ja nimi:
print("Piin-koodi masiina")
print("Tervetuloa! Tässä on kaksi mahtavaa (vaikka itse sanonkin) ohjelmaa Piihin ja pin-koodeihin liittyen.")
      
#Piin ensimmäiset tuhat numeroa
Pii = 3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198

#Muutetaan pii tekstiksi
Pii = str(Pii)

#Kysytään, että halutaanko Ohjelma 1 (Piin-koodi generaattori) vai Ohjelma 2 (Piin-koodi hirsipuu)
program = input("Haluatko ohjelman 1 (Piin-koodi generaattorin vai ohjelman 2 (Piin-koodi hirsipuu)? Vastaa numerolla 1 tai 2: ")

#Tässä jos koodin käyttäjä on laittanut jotain muuta kuin kaksi, ohjelma menee oletuksella ohjelmaksi 1. Esimerkiksi jos vastaisin äskeiseen '20', se muuttaisi sen ohjelmaksi 1.
try:
    if str(program) == "2":
        ohjelma = 2
    else:
        ohjelma = 1
        
except:
    ohjelma = 1
    
#Tarkistetaan, halutaanko ohjelma 1.
if ohjelma == 1:
    print("Tervetuloa! Jos käytät tätä koodia, haluat varmaan uuden pin-koodin. Tämä on erityinen ohjema. Se tuottaa 'Piin-koodin' eli se randomoi piin numeroista sinulle Pin-koodin. Sinun täytyy painaa vain enteriä, jos haluat Piin-koodin. Enjoy!")

    #Kerrotaan todennäköisyydet
    print("Tässä näkyy Piin-koodin eri numeroiden esiintymisen mahdollisuuset ja niiden määrä: ")
    print("Yhden todennäköisyys: " + str(Pii.count("1")/10) + "%" + "     " + "(" + str(Pii.count("1")) + ")")
    print("Kahden todennäköisyys: " + str(Pii.count("2")/10) + "%" + "    " + "(" + str(Pii.count("2")) + ")")
    print("Kolmen todennäköisyys: " + str(Pii.count("3")/10) + "%" + "    " + "(" + str(Pii.count("3")) + ")")
    print("Neljän todennäköisyys: " + str(Pii.count("4")/10) +"%" + "      " + "(" + str(Pii.count("4")) + ")")
    print("Viiden todennäköisyys: " + str(Pii.count("5")/10) + "%" + "      " + "(" + str(Pii.count("5")) + ")")
    print("Kuuden todennäköisyys: " + str(Pii.count("6")/10) + "%" + "      " + "(" + str(Pii.count("6")) + ")")
    print("Seitsemän todennäkoisyys: " + str(Pii.count("7")/10) + "%" + "   " +  "(" + str(Pii.count("7")) + ")")
    print("Kahdeksan todennäköisyys: " + str(Pii.count("8")/10) + "%" + " " +  "(" + str(Pii.count("8")) + ")")
    print("Yhdeksän todennäköisyys: " + str(Pii.count("9")/10) + "%" + "  " +  "(" + str(Pii.count("9")) + ")")
    print("Nollan todennäköisyys: " + str(Pii.count("0")/10) + "%" + "      "  + "(" + str(Pii.count("0")) + ")")

    #Piin-koodi silmukka
    while True:
        
        #Jos ei paineta enteriä, ohjelma sammuu
        Continue = input("")
        if Continue != "":
            break
        #Randomluvut
        R1 = random.randint(0,1000)
        R2 = random.randint(0,1000)
        R3 = random.randint(0,1000)
        R4 = random.randint(0,1000)
        #Otetaan luku piistä. Esim jos R1 = 3, Piistä (3.1415....) otetaan neljäs numero, eli 1.
        P1 = Pii[R1]
        P2 = Pii[R2]
        P3 = Pii[R3]
        P4 = Pii[R4]
        #Printataan pin-koodi

        print("'Piin'-koodi: " + str(P1) + str(P2) + str(P3) + str(P4))
    
#Ohjelma 2:
if ohjelma == 2:
    #Määritellään muuttujia
    voitot = 0
    häviöt = 0
    jatkuuko = ""
    print("Päätit sitten valita hirsipuuohjelman. Paina arvausnumeroasi ja enteriä. ")
    #Määritellään, että on peli numero yksi ja kerrotaan se.
    game = 1
    print("Peli #" + str(game) + ":")
    #Pelilooppi
    while True:
        #Myöhemmin kysytään, halutaanko jatkaa vai ei, tämä on toinen break siinä.
        if jatkuuko != "":
            break

        #Vaikeustason valinta
        Difficulty_level = input("Haluatko helpon (5 elämää), keskiverron (4 elämäää) vai vaikean (3 elämää)? Vastaa kirjaimella (H,K,V): ")
        
        if Difficulty_level == "H":
            Elämät = 5
        elif Difficulty_level == "K":
            Elämät = 4
        elif Difficulty_level == "V":
            Elämät = 3
        else:
            print("Teknisiä vaikeuksia. Sinulla on neljä elämää.")
            Elämät = 4

        print("Sinulla on " + str(Elämät) + " elämää.")
        #Randomluvut, joilla valitaan numerot Piin_koodiin
        R1 = random.randint(0,1000)
        R2 = random.randint(0,1000)
        R3 = random.randint(0,1000)
        R4 = random.randint(0,1000)
        #Määritellään Piin-koodi
        P1 = Pii[R1]
        P2 = Pii[R2]
        P3 = Pii[R3]
        P4 = Pii[R4]
        Piin_koodi = [int(P1),int(P2),int(P3),int(P4)]
        #Arvauksen tarkastamista varten
        arvausnumerot = [int(0),int(1),int(2),int(3),int(4),int(5),int(6),int(7),int(8),int(9)]
        wrongnumbers = []
        arvatutnumerot = []

        jatkuuko = ""
        #Arvauslooppi
        while True:
            #Tarkastetaan, onko arvattu kaikki numerot.
            if sorted(arvatutnumerot) == sorted(Piin_koodi):
                voitot += 1
                print("Voitit!")
                print("Piin_koodi: " + str(Piin_koodi))
                print("Olet voittanut " + str(voitot) + " kertaa ja hävinnyt " + str(häviöt) + " kertaa.")
                print("Uusi peli alkaa automaattisesti.")
                game += 1
                print("Peli #" + str(game) + ":")
                break
                
            #Jos hävittiin
            if Elämät == 0:
                # Lisätään pelattuihin peleihin ja häviöihin 1.
                game += 1
                häviöt += 1
                #Sanotaan että hävisit ja kerrotaan oikea koodi.
                print("Väärin meni, hävisit!")
                print("Oikea koodi: " + str(Piin_koodi))
                jatkuuko = input("Haluatko jatkaa? Paina enteristä jos haluat.")
                
                #Jos painetaan enteriä, hirsipuu alkaa alusta.
                if jatkuuko == "":
                    print("Peli #" + str(game) + ":")
                    break
                #Jos painetaan jotain muuta kuin enteriä, peli loppuu.
                else:
                    break
            #Kysytään arvaus
            arvaus = int(input("Arvaus: "))
            # Jos luku ei ole jo arvattu ja on vähemmän kuin 10, tarkistetaan, onko luku oikein vai väärin
            if arvaus not in arvatutnumerot and arvaus not in wrongnumbers and arvaus < 10:
                #Jos arvaus meni oikein, print("Oikein!")
                if arvaus in Piin_koodi:
                    if arvaus == int(P1):
                        
                        arvatutnumerot.append(int(arvaus))

                    if arvaus == int(P2):
                        
                        arvatutnumerot.append(int(arvaus))

                    if arvaus == int(P3):
                        
                        arvatutnumerot.append(int(arvaus))
                    if arvaus == int(P4):
                        
                        arvatutnumerot.append(int(arvaus))
                    print("Oikein!")
                    
                    print("Oikein arvatut numerot: " + str(arvatutnumerot))
                    print("Väärin arvatut numerot: " + str(wrongnumbers))
                    arvausnumerot.remove(arvaus)        
                    
                    
                #Jos arvaus meni väärin, miinusta yksi elämä ja print("Väärin! :(")
                elif arvaus not in Piin_koodi:
                    print("Väärin! :(")
                    #Lisätään väärien numeroiden listaan arvattu luku ja kerrotaan väärin ja oikein menneet numerot
                    wrongnumbers.append(arvaus)
                    print("Oikein arvatut numerot: " + str(arvatutnumerot))
                    print("Väärin arvatut numerot: " + str(wrongnumbers))
                    Elämät -= 1
                    #Kerrotaan, että paljonko elämiä on jäljellä.
                    if Elämät != 1:
                        print("Sinulla on " + str(Elämät) + " elämää.")
                    elif Elämät == 1:
                        print("Sinulla on enää yksi elämä.")
            #Jos arvaus on yli 10, siitä huomautetaan.
            elif arvaus > 10:
                print("Saat arvata vain yksinumeroisia.")
            #Jos arvaa saman numeron kuin on arvannut jo, ohjelma huomautaa siitä.
            else:
                print("Olet arvannut jo numeron " + str(arvaus) + ".")
