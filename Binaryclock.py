import time
print("Setting up the clock...")
time.sleep(5)
print("Binary clock!")
time.sleep(1)
print("This clock tells the time in bits!")
time.sleep(1)
seconds = int(input("How many binary seconds do you want to be added every real second?: "))
b = 0
while True:
    print(bin(b)[2:] + "  bits used: " + str(len(str(bin(b)))))
    b += seconds
    time.sleep(1)

