print("Potential energy caluculator")
while True:
    m = float(input("Enter the mass of an object in kg: "))
    g = float(input("Enter gravitation constant. Earth's gravitation constant is around 9.81: "))
    h = float(input("How high is the object relative to ground in meters? "))
    print("With that information, the potential energy of your object is " + str(m*g*h) + " J.")
