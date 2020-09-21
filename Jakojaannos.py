print("Jakojäännöslaskuri")
while True:
    x = input("Ensimmäinen luku: ") 
    y = input("Toinen luku: ")
    print("Jakojäännös: " + str(int(x) % int(y)))
    Continue = input("Paina enteriä jos haluat uudestaan.")
    if Continue != "":
        break
