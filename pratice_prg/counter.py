import time
tim = int(input("Enter the time duration: "))
for x in range(0,tim+1):
    print(f"{x} seconds")
    time.sleep(1)
print("Time is up ^-^")