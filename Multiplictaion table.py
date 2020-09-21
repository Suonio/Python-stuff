print("Multiplication table machine")
number = int(input("Enter the number to be multiplied: "))
times = int(input("Until what number do you want your number to be multiplied? "))
timestr = 0
for i in range(0,(times + 1)):
    print(str(number) + " * " + str(timestr) + " = " + str(number*timestr))
    timestr += 1
