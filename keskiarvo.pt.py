x = 0
y = 0
array = []
print("This machine can calculate the average of anything")
print("Insert your numbers. Press enter when you're done.")
while True:
    while True:
        z = input("Insert one number: ")
        if z != "":
            array.append(int(z))
        else:
            break

    for letter in array:
        x += array[y]
        y += 1
    print("Average: " + str(x/len(array)))
    print("")
