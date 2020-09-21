print("E = mc^2 calculator")
c = 299792458 ** 2
while True:
    whatToBeCalculated = input("Do you want to convert energy to mass (E) or mass to energy (m)? ")
    if whatToBeCalculated == "E":
        E = float(input("Energy in Joules: "))
        print("Energy converted to mass: " + str(E/c) + "kg")
    elif whatToBeCalculated == "m":
        m = float(input("Mass in kg: "))
        print("Mass converted to energy: " + str(m*c) + "J")
    else:
        print("False input. Try again.")
