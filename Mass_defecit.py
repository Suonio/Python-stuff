mp = 1.0072765
mn = 1.0086650
me = 0.0005485799
c = 299792458 ** 2
MeV = 6.24150913 * 10 ** 12
print("Mass defecit calculator")
protons = int(input("Enter the number of protons in the atom: "))
neutrons = int(input("Enter the number of neutrons in the atom: "))
electrons = int(input("Enter the number of electrons in the atom (Usually same as the number of protons): "))
atom = float(input("Enter the real mass of the atom in amu (u): "))
md = protons*mp+neutrons*mn+electrons*me-atom
ToKg = input("Do you want to convert the mass defecit to kg? (y/n): ")
if ToKg == "y":
    md = md * 1.6605402 * 10 ** -27
    ToJ = input("Do you want to convert the mass to Joules? (y/n): ")
    if ToJ == "y":
        ToMeV = input("Do you want to convert the binding energy to MeV? (y/n): ")
        if ToMeV == "y":
            ToMeVPN = input("Do you want to convert the binding energy to binding energy per nucleon? (y/n): ")
            if ToMeVPN == "y":
                print("Binding energy per nucleon: " + str(md*c*MeV/(protons+neutrons)))
            else:
                print("Binding energy: " + str(md*c*MeV) + " MeV")
        else:
            print("Binding energy: " + str(md*c) + "J")
    else:
        print("Mass defecit: " + md + "Kg")
else:
    print("Mass defecit: " + str(md) + "u")
